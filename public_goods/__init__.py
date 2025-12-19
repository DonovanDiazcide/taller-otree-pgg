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
    
    # Comprehension questions
    q1_endowment = models.IntegerField(
        label="What is your initial endowment in points?",
        choices=[50, 100, 150, 200],
    )
    
    q2_multiplier = models.FloatField(
        label="What is the efficiency factor (multiplier) for the group project?",
        choices=[1.5, 1.8, 2.0, 2.5],
    )
    
    q3_payoff = models.IntegerField(
        label="If you contribute 30 points and receive 45 points as your share from the group project, what is your final payoff?",
        choices=[85, 100, 115, 130],
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
    form_fields = ['q1_endowment', 'q2_multiplier', 'q3_payoff']
    
    def error_message(player, values):
        solutions = dict(
            q1_endowment=int(C.ENDOWMENT),
            q2_multiplier=float(C.MULTIPLIER),
            q3_payoff=115,  # 100 - 30 + 45 = 115
        )
        
        errors = {}
        for field_name in solutions:
            if values[field_name] != solutions[field_name]:
                errors[field_name] = 'Incorrect answer. Please try again.'
        
        if errors:
            return errors


class Contribute(Page):
    form_model = 'player'
    form_fields = ['contribution']


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs


class Results(Page):
    pass


page_sequence = [Introduction, Comprehension, Contribute, ResultsWaitPage, Results]
