from models import GameState, MoveEnum, Position, Battlesnake


def dist(p1: Position, p2: Position) -> int:
    return abs(p1.x - p2.x) + abs(p1.y - p2.y)


def all_dist(ps: list[Position], x: Position):
    return [dist(x, p) for p in ps]


def min_dist(ps: list[Position], x: Position):
    return min(all_dist(ps, x))


def make_move(state: GameState) -> MoveEnum:
    head = state.you.head
    food = state.board.food
    snakes = state.board.snakes
    used = set().union(*(s.body for s in snakes))
    deltas = {m: m.delta() for m in MoveEnum}
    choices = {}
    for m, d in deltas.items():
        new_pos = Position(x=head.x + d.x, y=head.y + d.y)
        if new_pos not in used:
            choices[m] = new_pos
    md = {m: min_dist(food, c) for m, c in choices.items()}

    return min(md.keys(), key=lambda m: md[m])


def move_snake(snake: Battlesnake, move: MoveEnum):
    head = snake.head
    delta = move.delta()
    new_head = Position(x=head.x + delta.x, y=head.y + delta.y)
    snake.body.insert(0, new_head)
    snake.body.pop()


def evaluate(state: GameState):
    head = state.you.head
    food = state.board.food
    return min_dist(food, head)
