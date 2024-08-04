import pytest

import models
from move import make_move


@pytest.fixture
def game_state():
    return models.GameState(
        game=models.Game(
            id="6884902f-a7a9-4fa5-ae95-d7efa6c7d8da",
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
        turn=104,
        board=models.Board(
            height=11,
            width=11,
            food=[models.Position(x=5, y=1), models.Position(x=1, y=4)],
            hazards=[],
            snakes=[
                models.Battlesnake(
                    id="gs_CHgkYrxyhKwkJpyv3bmMB3f4",
                    name="Incubating 🥚🥚🥚🥚",
                    health=25,
                    body=[
                        models.Position(x=4, y=8),
                        models.Position(x=4, y=7),
                        models.Position(x=4, y=6),
                        models.Position(x=4, y=5),
                        models.Position(x=4, y=4),
                    ],
                    latency="4",
                    head=models.Position(x=4, y=8),
                    length=5,
                    shout="🐍🐍🐍🐍",
                    squad="",
                    customizations=models.Customization(
                        color="#5a7576", head="cute-dragon", tail="default"
                    ),
                ),
                models.Battlesnake(
                    id="gs_krRg98dytGkMb8X8XCgykqgT",
                    name="Snake Guru",
                    health=96,
                    body=[
                        models.Position(x=7, y=7),
                        models.Position(x=7, y=8),
                        models.Position(x=7, y=9),
                        models.Position(x=8, y=9),
                        models.Position(x=8, y=10),
                        models.Position(x=9, y=10),
                        models.Position(x=9, y=9),
                        models.Position(x=9, y=8),
                        models.Position(x=8, y=8),
                        models.Position(x=8, y=7),
                        models.Position(x=8, y=6),
                        models.Position(x=7, y=6),
                        models.Position(x=6, y=6),
                        models.Position(x=6, y=7),
                        models.Position(x=6, y=8),
                        models.Position(x=6, y=9),
                        models.Position(x=6, y=10),
                        models.Position(x=5, y=10),
                        models.Position(x=4, y=10),
                        models.Position(x=3, y=10),
                    ],
                    latency="92",
                    head=models.Position(x=7, y=7),
                    length=20,
                    shout="",
                    squad="",
                    customizations=models.Customization(
                        color="#b62b2b", head="default", tail="default"
                    ),
                ),
            ],
        ),
        you=models.Battlesnake(
            id="gs_krRg98dytGkMb8X8XCgykqgT",
            name="Snake Guru",
            health=96,
            body=[
                models.Position(x=7, y=7),
                models.Position(x=7, y=8),
                models.Position(x=7, y=9),
                models.Position(x=8, y=9),
                models.Position(x=8, y=10),
                models.Position(x=9, y=10),
                models.Position(x=9, y=9),
                models.Position(x=9, y=8),
                models.Position(x=8, y=8),
                models.Position(x=8, y=7),
                models.Position(x=8, y=6),
                models.Position(x=7, y=6),
                models.Position(x=6, y=6),
                models.Position(x=6, y=7),
                models.Position(x=6, y=8),
                models.Position(x=6, y=9),
                models.Position(x=6, y=10),
                models.Position(x=5, y=10),
                models.Position(x=4, y=10),
                models.Position(x=3, y=10),
            ],
            latency="92",
            head=models.Position(x=7, y=7),
            length=20,
            shout="",
            squad="",
            customizations=models.Customization(
                color="#b62b2b", head="default", tail="default"
            ),
        ),
    )


def test_move_2(game_state):
    make_move(game_state)
