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
    q1_endowment = models.IntegerField(
        label="¿Cuál es la dotación inicial que recibe cada jugador?"
    )
    q2_multiplier = models.FloatField(
        label="¿Cuál es el factor de multiplicación aplicado a las contribuciones totales?"
    )
    q3_total_payoff = models.FloatField(
        label="Si cada jugador contribuye toda su dotación, ¿cuánto recibirá cada jugador del fondo común?"
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
class Comprehension(Page):
    form_model = 'player'
    form_fields = ['q1_endowment', 'q2_multiplier', 'q3_total_payoff']

    def error_message(player, values):
        solutions = dict(
            q1_endowment=C.ENDOWMENT,
            q2_multiplier=C.MULTIPLIER,
            q3_total_payoff=(C.ENDOWMENT * C.PLAYERS_PER_GROUP * C.MULTIPLIER) / C.PLAYERS_PER_GROUP,
        )

        errors = {}
        # Store which answers are correct for displaying success messages
        player.participant.vars['q1_correct'] = values['q1_endowment'] == solutions['q1_endowment']
        player.participant.vars['q2_correct'] = values['q2_multiplier'] == solutions['q2_multiplier']
        player.participant.vars['q3_correct'] = values['q3_total_payoff'] == solutions['q3_total_payoff']
        
        for field_name, expected_value in solutions.items():
            if values[field_name] != expected_value:
                errors[field_name] = f'❌ Incorrecto. Por favor, intenta de nuevo.'

        return errors

    def vars_for_template(player):
        # Get the correct answer flags from participant.vars (set in error_message)
        return dict(
            q1_correct=player.participant.vars.get('q1_correct', False),
            q2_correct=player.participant.vars.get('q2_correct', False),
            q3_correct=player.participant.vars.get('q3_correct', False),
        )


class Contribute(Page):
    form_model = 'player'
    form_fields = ['contribution']


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs


class Results(Page):
    pass


page_sequence = [Comprehension, Contribute, ResultsWaitPage, Results]
