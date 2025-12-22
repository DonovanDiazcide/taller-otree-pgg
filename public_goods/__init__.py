from otree.api import *
import json



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


page_sequence = [Contribute, ResultsWaitPage, Results]
