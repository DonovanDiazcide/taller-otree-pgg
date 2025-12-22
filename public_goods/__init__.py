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


# PAGES
class Contribute(Page):
    form_model = 'player'
    form_fields = ['contribution']


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs


class Results(Page):
    pass


page_sequence = [Contribute, ResultsWaitPage, Results]
