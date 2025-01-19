import random
from collections.abc import Iterator

from evaluate import evaluate
from models import GameState, MoveEnum, Position, Battlesnake


class InvalidMove(BaseException):
    pass


def make_move(state: GameState) -> MoveEnum:
    scores = [(m, evaluate(MoveEnum(m), state)) for m in MoveEnum]
    max_score = max(score for _, score in scores)
    return random.choice([m for m, s in scores if s == max_score])


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
