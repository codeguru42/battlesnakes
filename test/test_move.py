import models
import move


def test_move_snake_down(snake: models.Battlesnake):
    new_body = [
        models.Position(x=2, y=1),
        models.Position(x=2, y=2),
        models.Position(x=2, y=3),
    ]
    move.move_snake(snake, models.MoveEnum.DOWN)
    assert snake.body == new_body


def test_move_snake_left(snake: models.Battlesnake):
    new_body = [
        models.Position(x=1, y=2),
        models.Position(x=2, y=2),
        models.Position(x=2, y=3),
    ]
    move.move_snake(snake, models.MoveEnum.LEFT)
    assert snake.body == new_body


def test_move_snake_right(snake: models.Battlesnake):
    new_body = [
        models.Position(x=3, y=2),
        models.Position(x=2, y=2),
        models.Position(x=2, y=3),
    ]
    move.move_snake(snake, models.MoveEnum.RIGHT)
    assert snake.body == new_body
