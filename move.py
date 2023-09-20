import random

from models import GameState, MoveEnum, Position


def dist(p1: Position, p2: Position) -> int:
    return abs(p1.x - p2.x) + abs(p1.y - p2.y)


def all_dist(ps: list[Position], x: Position):
    return [dist(x, p) for p in ps]


def min_dist(ps: list[Position], x: Position):
    return min(all_dist(ps, x))


def make_move(state: GameState) -> MoveEnum:
    head = state.you.head
    food = state.board.food
    deltas = {m: m.delta() for m in MoveEnum}
    choices = {m: Position(x=head.x + d.x, y=head.y + d.y) for m, d in deltas.items()}
    md = {m: min_dist(food, c) for m, c in choices.items()}

    return min(md.keys(), key=lambda m: md[m])
