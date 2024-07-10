import pytest

import models


@pytest.fixture
def game_state(
    game: models.Game, turn: int, board: models.Board, snake: models.Battlesnake
):
    return models.GameState(game=game, turn=turn, board=board, you=snake)


@pytest.fixture
def game(ruleset: models.Ruleset):
    return models.Game(
        id="test_game", ruleset=ruleset, map="standard", timeout=30, source="tournament"
    )


@pytest.fixture
def ruleset(settings: models.RulesetSettings):
    return models.Ruleset(name="test_ruleset", version="1.0", settings=settings)


@pytest.fixture
def board(food, snakes):
    return models.Board(height=10, width=10, food=food, hazards=[], snakes=snakes)


@pytest.fixture
def snakes(snake):
    return [snake]


@pytest.fixture
def head(body):
    return body[0]


@pytest.fixture
def snake(body, head, customization):
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
        customizations=customization,
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


@pytest.fixture
def customization():
    return models.Customization(
        color="#B62B2B",
        head="default",
        tail="default",
    )
