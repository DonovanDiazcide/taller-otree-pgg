from otree.api import *

class C(BaseConstants):
    NAME_IN_URL = 'public_goods_simple'
    PLAYERS_PER_GROUP = 3
    NUM_ROUNDS = 1
    ENDOWMENT = cu(100)
    MULTIPLIER = 1.8

    # Constantes del sistema de castigo
    PUNISHMENT_COST = cu(1)        # Costo para quien castiga: 1 punto por cada punto de castigo
    PUNISHMENT_EFFECT = cu(3)      # Efecto en el castigado: pierde 3 puntos por cada punto de castigo recibido
    MAX_PUNISHMENT = 10            # Máximo de puntos de castigo que se pueden asignar a un jugador

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    total_contribution = models.CurrencyField()
    individual_share = models.CurrencyField()


class Player(BasePlayer):
    contribution = models.CurrencyField(
        min=0, max=C.ENDOWMENT, label="How much will you contribute?"
    )
    # Campos de puntos de castigo asignados a otros jugadores
    # Cada jugador puede castigar a los otros miembros de su grupo
    punishment_to_1 = models.IntegerField(
        min=0,
        max=C.MAX_PUNISHMENT,
        initial=0,
        label="Puntos de castigo para Jugador 1"
    )
    
    punishment_to_2 = models.IntegerField(
        min=0,
        max=C.MAX_PUNISHMENT,
        initial=0,
        label="Puntos de castigo para Jugador 2"
    )
    
    punishment_to_3 = models.IntegerField(
        min=0,
        max=C.MAX_PUNISHMENT,
        initial=0,
        label="Puntos de castigo para Jugador 3"
    )
    
    # Campo para registrar el castigo total recibido de otros jugadores
    total_punishment_received = models.IntegerField(
        initial=0
    )
    
    # Campo para registrar el costo pagado por castigar a otros
    punishment_cost_paid = models.CurrencyField(
        initial=0
    )

# FUNCTIONS
def set_payoffs(group: Group):
    players = group.get_players()
    contributions = [p.contribution for p in players]
    group.total_contribution = sum(contributions)
    group.individual_share = (
        group.total_contribution * C.MULTIPLIER / C.PLAYERS_PER_GROUP
    )
    for p in players:
        p.payoff = C.ENDOWMENT - p.contribution + group.individual_share

def calculate_final_payoffs(group: Group):
    """
    Calcula las ganancias finales después de aplicar el sistema de castigo.
    
    Pasos:
    1. Calcular el castigo total recibido por cada jugador
    2. Calcular el costo pagado por castigar
    3. Actualizar el payoff final de cada jugador
    """
    players = group.get_players()
    
    # Paso 1: Calcular cuánto castigo recibió cada jugador
    for player in players:
        total_received = 0
        
        # Sumar castigos de todos los otros jugadores
        for other in players:
            if other.id_in_group != player.id_in_group:
                # Obtener el campo punishment_to_X donde X es el id del jugador actual
                punishment_field = getattr(other, f'punishment_to_{player.id_in_group}', 0)
                if punishment_field is None:
                    punishment_field = 0
                total_received += punishment_field
        
        # Guardar el castigo total recibido
        player.total_punishment_received = total_received
    
    # Paso 2 y 3: Calcular costos y actualizar payoffs
    for player in players:
        # Calcular el costo de castigar a otros
        total_punishment_given = 0
        
        for other in players:
            if other.id_in_group != player.id_in_group:
                punishment_field = getattr(player, f'punishment_to_{other.id_in_group}', 0)
                if punishment_field is None:
                    punishment_field = 0
                total_punishment_given += punishment_field
        
        # Costo de castigar (1 punto por cada punto de castigo asignado)
        player.punishment_cost_paid = total_punishment_given * C.PUNISHMENT_COST
        
        # Efecto del castigo recibido (3 puntos perdidos por cada punto recibido)
        punishment_effect_received = player.total_punishment_received * C.PUNISHMENT_EFFECT
        
        # Ganancia final = Ganancia antes del castigo - Costo de castigar - Efecto del castigo recibido
        player.payoff = player.payoff - player.punishment_cost_paid - punishment_effect_received
        
        # Asegurar que el payoff no sea negativo
        if player.payoff < 0:
            player.payoff = cu(0)

# PAGES
class Contribute(Page):
    form_model = 'player'
    form_fields = ['contribution']


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs

# Nueva página para mostrar resultados intermedios antes del castigo
class IntermediateResults(Page):
    """
    Página que muestra las contribuciones y ganancias de cada jugador
    ANTES de aplicar el sistema de castigo.
    Los jugadores pueden ver qué contribuyó cada miembro del grupo.
    """
    
    def vars_for_template(player: Player):
        """
        Prepara las variables para mostrar en la plantilla.
        Incluye información de todos los jugadores del grupo.
        """
        # Obtener todos los jugadores del grupo
        group = player.group
        players = group.get_players()
        
        # Crear lista con información de cada jugador
        players_info = []
        for p in players:
            players_info.append({
                'id_in_group': p.id_in_group,
                'contribution': p.contribution,
                'payoff_before_punishment': p.payoff,  # Ganancia ANTES del castigo
            })
        
        return dict(
            players_info=players_info,
            total_contribution=group.total_contribution,
            individual_share=group.individual_share,
            my_contribution=player.contribution,
            my_payoff_before_punishment=player.payoff,
        )

# Página para asignar castigos a otros jugadores
class Punishment(Page):
    """
    Página donde cada jugador puede asignar puntos de castigo
    a los otros miembros de su grupo.
    
    Cada punto de castigo cuesta C.PUNISHMENT_COST al castigador
    y reduce C.PUNISHMENT_EFFECT al jugador castigado.
    """
    
    form_model = 'player'
    
    def get_form_fields(player: Player):
        """
        Genera dinámicamente los campos del formulario.
        Cada jugador puede castigar a los otros (no a sí mismo).
        """
        # Obtener lista de otros jugadores (excluir al jugador actual)
        other_players = [p for p in player.group.get_players() if p.id_in_group != player.id_in_group]
        
        # Crear campos dinámicamente: punishment_to_1, punishment_to_2, etc.
        fields = [f'punishment_to_{p.id_in_group}' for p in other_players]
        
        return fields
    
    def error_message(player: Player, values):
        """
        Valida que los castigos asignados sean válidos:
        1. No exceder MAX_PUNISHMENT por jugador
        2. No castigarse a sí mismo
        3. Total de castigos no debe exceder la ganancia del jugador
        """
        errors = {}
        
        # Calcular el costo total del castigo
        total_punishment_assigned = sum([v for k, v in values.items() if v is not None])
        total_cost = total_punishment_assigned * C.PUNISHMENT_COST
        
        # Validar que el jugador tenga suficiente para pagar el castigo
        if total_cost > player.payoff:
            errors['__all__'] = (
                f'No tienes suficientes puntos para asignar todo este castigo. '
                f'Tu ganancia actual es {player.payoff} puntos, pero el costo total '
                f'del castigo que intentas asignar es {total_cost} puntos '
                f'({total_punishment_assigned} puntos × {C.PUNISHMENT_COST} por punto).'
            )
        
        # Validar cada campo individualmente
        for field_name, value in values.items():
            if value is not None and value > C.MAX_PUNISHMENT:
                errors[field_name] = f'El máximo de puntos de castigo es {C.MAX_PUNISHMENT}.'
        
        return errors
    
    def vars_for_template(player: Player):
        """
        Prepara información de otros jugadores para mostrar en la plantilla.
        """
        group = player.group
        other_players = [p for p in group.get_players() if p.id_in_group != player.id_in_group]
        
        # Crear lista con información de otros jugadores
        other_players_info = []
        for p in other_players:
            other_players_info.append({
                'id_in_group': p.id_in_group,
                'contribution': p.contribution,
                'payoff_before_punishment': p.payoff,
            })
        
        return dict(
            other_players_info=other_players_info,
            my_payoff_before_punishment=player.payoff,
            punishment_cost=C.PUNISHMENT_COST,
            punishment_effect=C.PUNISHMENT_EFFECT,
            max_punishment=C.MAX_PUNISHMENT,
        )


# WaitPage después de asignar castigos
class PunishmentWaitPage(WaitPage):
    """
    Espera a que todos los jugadores asignen sus castigos
    antes de calcular las ganancias finales.
    """
    
    after_all_players_arrive = 'calculate_final_payoffs'
    
    title_text = "Por favor espera"
    body_text = "Esperando a que todos los jugadores asignen sus castigos..."

class Results(Page):
    pass


page_sequence = [Contribute, ResultsWaitPage, Results]
