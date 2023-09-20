import random
from enum import StrEnum


class MoveEnum(StrEnum):
    UP = 'up'
    DOWN = 'down'
    LEFT = 'left'
    RIGHT = 'right'


def make_move() -> MoveEnum:
    return random.choice(list(MoveEnum))
