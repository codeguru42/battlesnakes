import pytest

import models
import move


@pytest.fixture
def other_snakes(other):
    return {other}


@pytest.fixture
def other_body():
    return [
        models.Position(x=3, y=1),
        models.Position(x=4, y=1),
    ]


def test_will_win_head_to_head(me, other_snakes):
    pos = models.Position(x=3, y=2)
    assert move.will_win_head_to_head(pos, me, other_snakes)
