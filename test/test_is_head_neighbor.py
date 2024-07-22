import pytest

import models
from move import is_head_neighbor


@pytest.fixture
def snakes(me, other):
    return [me, other]


def test_is_head_neighbor(other: models.Battlesnake, me: models.Battlesnake):
    assert is_head_neighbor(other, models.Position(x=3, y=2))
