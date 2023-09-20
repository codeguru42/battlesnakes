import random

from models import GameState, MoveEnum, Position


def dist(p1, p2):
    return abs(p1.x - p2.x) + abs(p1.y - p2.y)


def make_move(state: GameState) -> MoveEnum:
    head = state.you.head
    food = state.board.food
    deltas = {m: m.delta() for m in MoveEnum}
    choices = {m: Position(x=head.x + d.x, y=head.y + d.y) for m, d in deltas.items()}
    min_dist = {m: min(dist(c, f) for f in food) for m, c in choices.items()}

    return min(min_dist.keys(), key=lambda m: min_dist[m])
