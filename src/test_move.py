import pytest

import models
import move


@pytest.fixture
def game_state(
    game: models.Game, turn: int, board: models.Board, you: models.Battlesnake
):
    return models.GameState(game=game, turn=turn, board=board, you=you)


@pytest.fixture
def game(ruleset: models.Ruleset):
    return models.Game(
        id="test_game", ruleset=ruleset, map="standard", timeout=30, source="tournament"
    )


@pytest.fixture
def ruleset(settings: models.RulesetSettings):
    return models.Ruleset(name="test_ruleset", version="1.0", settings=settings)


@pytest.fixture
def board(food, snakes, you):
    return models.Board(height=10, width=10, food=food, hazards=[], snakes=snakes)


@pytest.fixture
def you(body, metadata):
    head = body[0]
    return models.Battlesnake(
        id="1",
        name="test_snake",
        health=100,
        body=body,
        latency="10ms",
        head=head,
        length=len(body),
        shout="",
        squad="",
        customizations=metadata,
    )


@pytest.fixture
def body():
    return [
        models.Position(x=2, y=2),
        models.Position(x=2, y=3),
        models.Position(x=2, y=4),
    ]


@pytest.fixture
def metadata():
    return models.MetaData(
        apiversion="1",
        author="codeguru42",
        color="#B62B2B",
        head="default",
        tail="default",
        version="0.0.1-beta",
    )


def test_move_snake_down(you):
    new_body = [
        models.Position(x=2, y=1),
        models.Position(x=2, y=2),
        models.Position(x=2, y=3),
    ]
    move.move_snake(you, models.MoveEnum.DOWN)
    assert you.body == new_body


def test_move_snake_left(you):
    new_body = [
        models.Position(x=1, y=2),
        models.Position(x=2, y=2),
        models.Position(x=2, y=3),
    ]
    move.move_snake(you, models.MoveEnum.LEFT)
    assert you.body == new_body


def test_move_snake_right(you):
    new_body = [
        models.Position(x=3, y=2),
        models.Position(x=2, y=2),
        models.Position(x=2, y=3),
    ]
    move.move_snake(you, models.MoveEnum.RIGHT)
    assert you.body == new_body
