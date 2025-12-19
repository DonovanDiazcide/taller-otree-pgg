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
    q1_endowment = models.CurrencyField(
        label="¿Cuál es la dotación inicial que recibe cada jugador?"
    )
    q2_multiplier = models.FloatField(
        label="¿Cuál es el factor de multiplicación aplicado a las contribuciones totales?"
    )
    q3_total_payoff = models.CurrencyField(
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
            q3_total_payoff=C.ENDOWMENT * C.MULTIPLIER,
        )
        
        # Map field names to their short variable names for the template
        field_to_var = {
            'q1_endowment': 'q1',
            'q2_multiplier': 'q2',
            'q3_total_payoff': 'q3',
        }

        errors = {}
        # Store which answers are correct for displaying success messages
        for field_name in solutions:
            var_name = field_to_var[field_name]
            player.participant.vars[f'{var_name}_correct'] = values[field_name] == solutions[field_name]
            if values[field_name] != solutions[field_name]:
                errors[field_name] = f'❌ Incorrecto. Por favor, intenta de nuevo.'

        return errors

    def vars_for_template(player):
        # Get the correct answer flags from participant.vars (set in error_message)
        return {
            f'q{i}_correct': player.participant.vars.get(f'q{i}_correct', False)
            for i in [1, 2, 3]
        }


class Contribute(Page):
    form_model = 'player'
    form_fields = ['contribution']


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs


class Results(Page):
    pass


page_sequence = [Comprehension, Contribute, ResultsWaitPage, Results]
