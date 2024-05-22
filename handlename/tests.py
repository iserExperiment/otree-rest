from typing import Callable, Type

import handlename as pages
from . import *

import random

random.seed(1111)


class PlayerBot(Bot):
    def play_round(self):
        yield Submission(
            pages.Login,
            dict(
                handlename= 'ボット{:03}'.format(random.randint(1, 999))
            ),
            check_html=False, timeout_happened=False,
        )
