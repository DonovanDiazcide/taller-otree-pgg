from otree.api import *

class C(BaseConstants):
    NAME_IN_URL = 'public_goods_simple'
    PLAYERS_PER_GROUP = 3
    NUM_ROUNDS = 4
    ENDOWMENT = cu(100)
    MULTIPLIER = 1.8


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


class Results(Page):
    pass




page_sequence = [Introduction, Comprehension, Contribute, ResultsWaitPage, Results]
