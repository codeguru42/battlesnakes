import models
import move


def test_all_moves(snake: models.Battlesnake):
    expected = [
        snake.model_copy(
            update={
                "head": models.Position(x=2, y=1),
                "body": [
                    models.Position(x=2, y=1),
                    models.Position(x=2, y=2),
                    models.Position(x=2, y=3),
                ],
            }
        ),
        snake.model_copy(
            update={
                "head": models.Position(x=1, y=2),
                "body": [
                    models.Position(x=1, y=2),
                    models.Position(x=2, y=2),
                    models.Position(x=2, y=3),
                ],
            }
        ),
        snake.model_copy(
            update={
                "head": models.Position(x=3, y=2),
                "body": [
                    models.Position(x=3, y=2),
                    models.Position(x=2, y=2),
                    models.Position(x=2, y=3),
                ],
            }
        ),
    ]

    actual = [snake.model_copy(deep=True) for snake in move.all_moves(snake)]
    assert actual == expected
