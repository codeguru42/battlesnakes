from collections.abc import Iterator

from models import GameState, MoveEnum, Position, Battlesnake


class InvalidMove(BaseException):
    pass


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
    used = set().union(*(s.body[:-1] for s in snakes))
    deltas = {MoveEnum(m): MoveEnum(m).delta() for m in MoveEnum}
    choices = {}
    for m, d in deltas.items():
        new_pos = Position(x=head.x + d.x, y=head.y + d.y)
        if is_in_bounds(
            new_pos, state.board.width, state.board.height
        ) and not is_occupied(new_pos, used):
            choices[m] = new_pos
    md = {m: min_dist(food, c) for m, c in choices.items()}

    return min(md.keys(), key=lambda m: md[m])


def is_in_bounds(pos: Position, width: int, height: int) -> bool:
    return 0 <= pos.x < width and 0 <= pos.y < height


def is_occupied(pos: Position, used: set[Position]) -> bool:
    return pos in used


def move_snake(snake: Battlesnake, move: MoveEnum) -> Position:
    head = snake.head
    delta = move.delta()
    new_head = Position(x=head.x + delta.x, y=head.y + delta.y)

    if new_head == snake.body[1]:
        raise InvalidMove

    snake.head = new_head
    snake.body.insert(0, new_head)
    return snake.body.pop()


def unmove_snake(snake: Battlesnake, prev_tail: Position):
    snake.body.pop(0)
    snake.head = snake.body[0]
    snake.body.append(prev_tail)


def all_moves(snake: Battlesnake) -> Iterator[Battlesnake]:
    for m in MoveEnum:
        try:
            prev_tail = move_snake(snake, MoveEnum(m))
            yield snake
            unmove_snake(snake, prev_tail)
        except InvalidMove:
            pass


def evaluate(state: GameState):
    head = state.you.head
    food = state.board.food
    return min_dist(food, head)
