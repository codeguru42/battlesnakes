import random

from models import MoveEnum


def make_move() -> MoveEnum:
    return random.choice(list(MoveEnum))
