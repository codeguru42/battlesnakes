import pytest

import models
from move import make_move


@pytest.fixture
def game_state():
    return models.GameState(
        game=models.Game(
            id="10a73e2c-7c49-4480-b27a-639207057cce",
            ruleset=models.Ruleset(
                name="standard",
                version="v1.2.3",
                settings=models.RulesetSettings(
                    foodSpawnChance=15,
                    minimumFood=1,
                    hazardDamagePerTurn=0,
                    royale=models.RoyaleSettings(shrinkEveryNTurns=0),
                    squad=models.SquadSettings(
                        allowBodyCollisions=False,
                        sharedElimination=False,
                        sharedHealth=False,
                        sharedLength=False,
                    ),
                ),
            ),
            map="standard",
            timeout=500,
            source="ladder",
        ),
        turn=53,
        board=models.Board(
            height=11,
            width=11,
            food=[models.Position(x=9, y=9)],
            hazards=[],
            snakes=[
                models.Battlesnake(
                    id="gs_BbmmFvbyCY4Hv7VyF6kJkWrX",
                    name="Hunger of Hadar",
                    health=99,
                    body=[
                        models.Position(x=0, y=7),
                        models.Position(x=0, y=6),
                        models.Position(x=1, y=6),
                        models.Position(x=2, y=6),
                        models.Position(x=2, y=7),
                        models.Position(x=3, y=7),
                        models.Position(x=3, y=6),
                        models.Position(x=3, y=5),
                        models.Position(x=3, y=4),
                    ],
                    latency="15",
                    head=models.Position(x=0, y=7),
                    length=9,
                    shout="",
                    squad="",
                    customizations=models.Customization(
                        color="#660000", head="chomp", tail="ghost"
                    ),
                ),
                models.Battlesnake(
                    id="gs_Q9tHRftKGbvGYBDRTqdRjtgM",
                    name="alpha",
                    health=86,
                    body=[
                        models.Position(x=4, y=1),
                        models.Position(x=5, y=1),
                        models.Position(x=6, y=1),
                        models.Position(x=6, y=2),
                        models.Position(x=6, y=3),
                        models.Position(x=7, y=3),
                        models.Position(x=7, y=4),
                        models.Position(x=8, y=4),
                    ],
                    latency="97",
                    head=models.Position(x=4, y=1),
                    length=8,
                    shout="",
                    squad="",
                    customizations=models.Customization(
                        color="#3e338f", head="evil", tail="flame"
                    ),
                ),
                models.Battlesnake(
                    id="gs_tRqf4vf84Q9qyhGpmR4GkwG6",
                    name="Snake Guru",
                    health=90,
                    body=[
                        models.Position(x=2, y=5),
                        models.Position(x=2, y=4),
                        models.Position(x=2, y=3),
                        models.Position(x=2, y=2),
                        models.Position(x=2, y=1),
                        models.Position(x=2, y=0),
                        models.Position(x=1, y=0),
                        models.Position(x=1, y=1),
                        models.Position(x=1, y=2),
                    ],
                    latency="87",
                    head=models.Position(x=2, y=5),
                    length=9,
                    shout="",
                    squad="",
                    customizations=models.Customization(
                        color="#b62b2b", head="default", tail="default"
                    ),
                ),
            ],
        ),
        you=models.Battlesnake(
            id="gs_tRqf4vf84Q9qyhGpmR4GkwG6",
            name="Snake Guru",
            health=90,
            body=[
                models.Position(x=2, y=5),
                models.Position(x=2, y=4),
                models.Position(x=2, y=3),
                models.Position(x=2, y=2),
                models.Position(x=2, y=1),
                models.Position(x=2, y=0),
                models.Position(x=1, y=0),
                models.Position(x=1, y=1),
                models.Position(x=1, y=2),
            ],
            latency="87",
            head=models.Position(x=2, y=5),
            length=9,
            shout="",
            squad="",
            customizations=models.Customization(
                color="#b62b2b", head="default", tail="default"
            ),
        ),
    )


def test_move_2(game_state):
    make_move(game_state)
