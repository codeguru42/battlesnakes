import pytest

import models
from move import is_head_neighbor


@pytest.fixture
def snakes(me, other):
    return [me, other]


@pytest.fixture
def body():
    return [
        models.Position(x=2, y=2),
        models.Position(x=2, y=3),
        models.Position(x=2, y=4),
    ]


@pytest.fixture
def me(head, body, customization):
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
def other_body():
    return [
        models.Position(x=3, y=1),
        models.Position(x=4, y=1),
        models.Position(x=5, y=1),
    ]


@pytest.fixture
def other_head(other_body):
    return other_body[0]


@pytest.fixture
def other(other_body, other_head, customization):
    return models.Battlesnake(
        id="2",
        name="other_snake",
        health=100,
        body=other_body,
        latency="10ms",
        head=other_head,
        length=len(other_body),
        shout="",
        squad="",
        customizations=customization,
    )


def test_is_head_neighbor(snakes: list[models.Battlesnake], me: models.Battlesnake):
    assert is_head_neighbor(snakes, me.head)
