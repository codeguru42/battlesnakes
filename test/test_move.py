import models
import move


def test_move_snake_down(you: models.Battlesnake):
    new_body = [
        models.Position(x=2, y=1),
        models.Position(x=2, y=2),
        models.Position(x=2, y=3),
    ]
    move.move_snake(you, models.MoveEnum.DOWN)
    assert you.body == new_body


def test_move_snake_left(you: models.Battlesnake):
    new_body = [
        models.Position(x=1, y=2),
        models.Position(x=2, y=2),
        models.Position(x=2, y=3),
    ]
    move.move_snake(you, models.MoveEnum.LEFT)
    assert you.body == new_body


def test_move_snake_right(you: models.Battlesnake):
    new_body = [
        models.Position(x=3, y=2),
        models.Position(x=2, y=2),
        models.Position(x=2, y=3),
    ]
    move.move_snake(you, models.MoveEnum.RIGHT)
    assert you.body == new_body
