import random
from enum import StrEnum


class Move(StrEnum):
    UP = 'up'
    DOWN = 'down'
    LEFT = 'left'
    RIGHT = 'right'


def make_move() -> Move:
    return random.choice(list(Move))
