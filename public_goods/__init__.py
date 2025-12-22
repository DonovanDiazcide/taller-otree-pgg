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
    contribution = models.CurrencyField(
        min=0, max=C.ENDOWMENT, label="How much will you contribute?"
    )
     # Pregunta de comprensión 1
    comp_q1 = models.IntegerField(
        #models.IntegerField indica que el usuario debe responder con un número entero
        label="¿Cuántos puntos recibe cada jugador por cada punto aportado al fondo?",
        #label es el texto que ve el participante
    )

    # Pregunta de comprensión 2
    comp_q2 = models.IntegerField(
        label="Si los 3 jugadores aportan 50 cada uno, ¿cuánto hay en el fondo común?",
        choices=[
            [50, '50'],
            [100, '100'],
            [150, '150'],
            [200, '200'],
        ]
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
