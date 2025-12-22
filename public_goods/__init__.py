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


# FUNCTIONS
def get_config_value(session, key, default):
    return session.config.get(key, default)

def set_payoffs(group: Group):
    players = group.get_players()
    contributions = [p.contribution for p in players]
    group.total_contribution = sum(contributions)
    multiplier = get_config_value(group, 'multiplier', default=C.MULTIPLIER, cast=float)
    n_players = len(players)
    group.individual_share = group.total_contribution * multiplier / n_players
    for p in players:
        p.payoff = C.ENDOWMENT - p.contribution + group.individual_share


# PAGES
class Contribute(Page):
    form_model = 'player'
    form_fields = ['contribution']
 def vars_for_template(self):

        treatment = get_config_value(self, 'treatment', default='baseline')
        multiplier = get_config_value(self, 'multiplier', default=C.MULTIPLIER, cast=float)
        note_players_per_group = C.PLAYERS_PER_GROUP
        mpcr = multiplier / note_players_per_group

        return dict(
            treatment=treatment,
            multiplier=multiplier,
            mpcr=mpcr,
            endowment=C.ENDOWMENT,
            players_per_group=note_players_per_group,
        )

class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs


class Results(Page):
    pass


page_sequence = [Contribute, ResultsWaitPage, Results]
