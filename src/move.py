from collections.abc import Iterator

from evaluate import evaluate
from models import GameState, MoveEnum, Position, Battlesnake


class InvalidMove(BaseException):
    pass


def make_move(state: GameState) -> MoveEnum:
    return max((MoveEnum(m) for m in MoveEnum), key=lambda m: evaluate(m, state))


def dist(p1: Position, p2: Position) -> int:
    return abs(p1.x - p2.x) + abs(p1.y - p2.y)


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


def is_head_neighbor(snake: Battlesnake, pos: Position) -> bool:
    return dist(snake.head, pos) == 1


def is_longer(snake: Battlesnake, other: Battlesnake) -> bool:
    return snake.length > other.length


def will_win_head_to_head(
    pos: Position, you: Battlesnake, other_snakes: set[Battlesnake]
) -> bool:
    return all(
        not is_head_neighbor(other, pos) or is_longer(you, other)
        for other in other_snakes
    )
