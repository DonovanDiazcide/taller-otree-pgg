from otree.api import *

class C(BaseConstants):
    NAME_IN_URL = 'public_goods_simple'
    PLAYERS_PER_GROUP = 3
    NUM_ROUNDS = 1
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
    
    # Comprehension question fields
    q1_endowment = models.IntegerField(
        label="Tu respuesta:",
        min=0
    )
    q2_multiplier = models.FloatField(
        label="Tu respuesta:",
        min=0,
        max=10
    )
    q3_full_contribution = models.IntegerField(
        label="Tu respuesta:",
        min=0
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
class Introduction(Page):
    pass


class Comprehension(Page):
    form_model = 'player'
    form_fields = ['q1_endowment', 'q2_multiplier', 'q3_full_contribution']
    
    def error_message(player, values):
        errors = {}
        
        # Check question 1: endowment should be 100
        if values['q1_endowment'] != C.ENDOWMENT:
            errors['q1_endowment'] = '❌ Respuesta incorrecta. Por favor intenta de nuevo.'
        
        # Check question 2: multiplier should be 1.8 (with tolerance for floating point)
        if abs(values['q2_multiplier'] - float(C.MULTIPLIER)) > 0.01:
            errors['q2_multiplier'] = '❌ Respuesta incorrecta. Por favor intenta de nuevo.'
        
        # Check question 3: if everyone contributes 100, each gets (300 * 1.8) / 3 = 180
        expected_share = (C.ENDOWMENT * C.PLAYERS_PER_GROUP * C.MULTIPLIER) / C.PLAYERS_PER_GROUP
        if values['q3_full_contribution'] != expected_share:
            errors['q3_full_contribution'] = '❌ Respuesta incorrecta. Por favor intenta de nuevo.'
        
        return errors


class Contribute(Page):
    form_model = 'player'
    form_fields = ['contribution']


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs


class Results(Page):
    pass


page_sequence = [Introduction, Comprehension, Contribute, ResultsWaitPage, Results]
