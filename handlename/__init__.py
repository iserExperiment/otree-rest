from otree.api import *
import random
import os


class C(BaseConstants):
    NAME_IN_URL = "handlename"
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    studentid = models.StringField(label="学籍番号を入力してください．")
    handlename = models.StringField(label="ハンドルネームを入力してください．")


# PAGES
class Login(Page):
    form_model = "player"

    @staticmethod
    def get_form_fields(player: Player):
        if player.session.config["input_id"]:
            return ["studentid", "handlename"]
        return ["handlename"]

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if not player.participant.vars.get("handlename"):
            if timeout_happened:
                player.handlename = "名無し{:03}".format(random.randint(1, 999))
            player.participant.handlename = player.handlename

        if player.session.config["input_id"]:
            if player.field_maybe_none("studentid"):
                player.participant.studentid = player.studentid
        else:
            if player.participant.label:
                player.participant.studentid = player.participant.label


page_sequence = [Login]


def vars_for_admin_report(subsession: Subsession):
    return dict(
        deadlist=[
            [p.participant.id_in_session, p.participant.code]
            for p in subsession.get_players()
            if (
                (not p.participant.label)
                and (p.participant.vars.get("studentid", None) is None)
            )
        ],
        revivallist=[
            [p.participant.id_in_session, p.participant.code, p.participant.studentid]
            for p in subsession.get_players()
            if (
                (not p.participant.label)
                and (p.participant.vars.get("studentid", None) is not None)
            )
        ],
        REST_KEY=os.environ.get("OTREE_REST_KEY", ""),
    )
