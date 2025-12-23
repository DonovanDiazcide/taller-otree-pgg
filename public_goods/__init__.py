from otree.api import *
import json



class C(BaseConstants):
    NAME_IN_URL = 'public_goods_simple'
    PLAYERS_PER_GROUP = 3
    NUM_ROUNDS = 4
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
    # Campo de contribución (ya existente)
    contribution = models.CurrencyField(
        min=0,
        max=C.ENDOWMENT,
        label="¿Cuánto quieres contribuir al fondo común?"
    )
    
    # NUEVOS CAMPOS: Preguntas de comprensión
    comp_q1 = models.IntegerField(
        label="¿Cuántos puntos recibe cada jugador al inicio de la ronda?"
    )
    
    comp_q2 = models.IntegerField(
        label="Si los 3 jugadores contribuyen 50 puntos cada uno, ¿cuánto habrá en el fondo común ANTES de multiplicar?",
        choices=[
            [50, '50 puntos'],
            [100, '100 puntos'],
            [150, '150 puntos'],
            [200, '200 puntos'],
        ]
    )
    
    comp_q3 = models.IntegerField(
        label="Si el fondo común tiene 300 puntos después de multiplicar, ¿cuánto recibe CADA jugador del fondo?",
        choices=[
            [50, '50 puntos'],
            [100, '100 puntos'],
            [150, '150 puntos'],
            [300, '300 puntos'],
        ]
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
def get_config_value(session, key, default):
    return session.config.get(key, default)

def set_payoffs(group: Group):
    session = group.session
    
    endowment = get_config_value(session, 'endowment', C.ENDOWMENT)
    multiplier = get_config_value(session, 'multiplier', C.MULTIPLIER)
    n_players = get_config_value(session, 'players_per_group', C.PLAYERS_PER_GROUP)
    
    players = group.get_players()
    contributions = [p.contribution for p in players]
    
    group.total_contribution = sum(contributions)
    group.individual_share = (group.total_contribution * multiplier) / n_players
    
    for p in players:
        p.payoff = endowment - p.contribution + group.individual_share

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
class Introduction(Page):
    pass

class Comprehension(Page):
    """Página de preguntas de comprensión con validación"""
    form_model = 'player'
    form_fields = ['comp_q1', 'comp_q2', 'comp_q3']
    
    @staticmethod
    def error_message(player, values):
        # Respuestas correctas
        soluciones = {
            'comp_q1': 100,  # Dotación inicial
            'comp_q2': 150,  # 3 jugadores × 50 = 150
            'comp_q3': 100,  # 300 ÷ 3 = 100
        }
        
        errores = []
        
        if values['comp_q1'] != soluciones['comp_q1']:
            errores.append("Pregunta 1: La respuesta correcta es 100 puntos.")
        
        if values['comp_q2'] != soluciones['comp_q2']:
            errores.append("Pregunta 2: Recuerda que hay 3 jugadores y cada uno contribuye 50.")
        
        if values['comp_q3'] != soluciones['comp_q3']:
            errores.append("Pregunta 3: El fondo se divide equitativamente entre los 3 jugadores.")
        
        if errores:
            return ' '.join(errores)
class Contribute(Page):
    """Página donde el jugador decide su contribución"""
    form_model = 'player'
    form_fields = ['contribution']
    
    @staticmethod
    def vars_for_template(player):
        """Pasa los parámetros del tratamiento al template"""
        session = player.session
        endowment = get_config_value(session, 'endowment', C.ENDOWMENT)
        multiplier = get_config_value(session, 'multiplier', C.MULTIPLIER)
        n_players = get_config_value(session, 'players_per_group', C.PLAYERS_PER_GROUP)
        
        # Calcular MPCR para mostrar
        mpcr = round(multiplier / n_players, 2)
        
        return dict(
            endowment=endowment,
            multiplier=multiplier,
            n_players=n_players,
            mpcr=mpcr,
        )


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

# Página de resultados finales con desglose del castigo
class FinalResults(Page):
    """
    Página que muestra los resultados finales del experimento
    incluyendo el desglose completo del sistema de castigo.
    """
    
    def vars_for_template(player: Player):
        """
        Prepara todas las variables necesarias para mostrar
        el desglose detallado de ganancias y castigos.
        """
        group = player.group
        
        # Información de todos los jugadores para la tabla
        players_info = []
        for p in group.get_players():
            # Calcular ganancia antes del castigo (endowment - contribución + participación)
            payoff_before_punishment = C.ENDOWMENT - p.contribution + group.individual_share
            
            # Calcular total de castigos dados por este jugador
            punishment_given = 0
            for other in group.get_players():
                if other.id_in_group != p.id_in_group:
                    punishment_field = getattr(p, f'punishment_to_{other.id_in_group}', 0)
                    if punishment_field is None:
                        punishment_field = 0
                    punishment_given += punishment_field
            
            players_info.append({
                'id_in_group': p.id_in_group,
                'contribution': p.contribution,
                'payoff_before_punishment': payoff_before_punishment,
                'punishment_given': punishment_given,
                'punishment_cost': p.punishment_cost_paid,
                'punishment_received': p.total_punishment_received,
                'punishment_effect': p.total_punishment_received * C.PUNISHMENT_EFFECT,
                'final_payoff': p.payoff,
            })
        
        # Calcular información específica del jugador actual
        my_payoff_before_punishment = C.ENDOWMENT - player.contribution + group.individual_share
        
        # Calcular castigos dados por el jugador actual a cada otro jugador
        my_punishments_given = []
        for other in group.get_players():
            if other.id_in_group != player.id_in_group:
                punishment_amount = getattr(player, f'punishment_to_{other.id_in_group}', 0)
                if punishment_amount is None:
                    punishment_amount = 0
                if punishment_amount > 0:  # Solo mostrar si hubo castigo
                    my_punishments_given.append({
                        'target_id': other.id_in_group,
                        'amount': punishment_amount,
                        'cost': punishment_amount * C.PUNISHMENT_COST,
                    })
        
        # Calcular castigos recibidos por el jugador actual de cada otro jugador
        my_punishments_received = []
        for other in group.get_players():
            if other.id_in_group != player.id_in_group:
                punishment_amount = getattr(other, f'punishment_to_{player.id_in_group}', 0)
                if punishment_amount is None:
                    punishment_amount = 0
                if punishment_amount > 0:  # Solo mostrar si hubo castigo
                    my_punishments_received.append({
                        'from_id': other.id_in_group,
                        'amount': punishment_amount,
                        'effect': punishment_amount * C.PUNISHMENT_EFFECT,
                    })
        
        return dict(
            players_info=players_info,
            # Información del grupo
            total_contribution=group.total_contribution,
            individual_share=group.individual_share,
            # Información del jugador actual - Fase 1
            my_contribution=player.contribution,
            my_payoff_before_punishment=my_payoff_before_punishment,
            # Información del jugador actual - Castigos dados
            my_punishments_given=my_punishments_given,
            my_total_punishment_cost=player.punishment_cost_paid,
            # Información del jugador actual - Castigos recibidos
            my_punishments_received=my_punishments_received,
            my_total_punishment_received=player.total_punishment_received,
            my_total_punishment_effect=player.total_punishment_received * C.PUNISHMENT_EFFECT,
            # Ganancia final
            my_final_payoff=player.payoff,
            # Constantes para referencia
            endowment=C.ENDOWMENT,
            multiplier=C.MULTIPLIER,
            punishment_cost=C.PUNISHMENT_COST,
            punishment_effect=C.PUNISHMENT_EFFECT,
        )

class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        players = group.get_players()

        # 1) Datos para la tabla (una fila por jugador)
        contributions_table = [
            {"id_in_group": p.id_in_group, "contribution": p.contribution}
            for p in players
        ]

        # 2) Datos para el gráfico (JSON listo para Chart.js)
        chart_labels_json = json.dumps([f"Player {p.id_in_group}" for p in players])
        chart_values_json = json.dumps([float(p.contribution) for p in players])

        # 3) Datos para el desglose del payoff
        breakdown = {
            "endowment": C.ENDOWMENT,
            "your_contribution": player.contribution,
            "total_contribution": group.total_contribution,
            "multiplier": C.MULTIPLIER,
            "players_per_group": C.PLAYERS_PER_GROUP,
            "individual_share": group.individual_share,
            "payoff": player.payoff,
        }

        return {
            "contributions_table": contributions_table,
            "chart_labels_json": chart_labels_json,
            "chart_values_json": chart_values_json,
            "breakdown": breakdown,
        }

      
      # falta resolver estos conflictos. 
page_sequence = [Introduction, Comprehension, Contribute, ResultsWaitPage, Results]




