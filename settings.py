from os import environ


SESSION_CONFIGS = [
    dict(
        name="classroom",
        app_sequence=["handlename", "prisoner"],
        num_demo_participants=2,
    )
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00,
    participation_fee=0.00,
    doc="",
    input_id=False,
    count_dead=False,
)

PARTICIPANT_FIELDS = ["handlename", "studentid"]
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = "ja"

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = "JPY"
USE_POINTS = True

ROOMS = [
    dict(
        name="SUB",
        display_name="SUB",
        participant_label_file="_rooms/SUB.txt",
    )
]

ADMIN_USERNAME = "admin"
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get("OTREE_ADMIN_PASSWORD")

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = "1255233045211"
