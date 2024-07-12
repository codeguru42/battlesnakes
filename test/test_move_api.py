import pytest

import models
import move


@pytest.fixture
def game_state():
    return models.GameState(
        game=models.Game(
            id="7e8875be-cb25-489d-82dd-6efab5422fb5",
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
        turn=5,
        board=models.Board(
            height=11,
            width=11,
            food=[models.Position(x=6, y=0), models.Position(x=5, y=5)],
            hazards=[],
            snakes=[
                models.Battlesnake(
                    id="gs_4J74kWtFctdKqfXbV4dXwtFH",
                    name="JKSnake2",
                    health=95,
                    body=[
                        models.Position(x=5, y=0),
                        models.Position(x=5, y=1),
                        models.Position(x=4, y=1),
                    ],
                    latency="88",
                    head=models.Position(x=5, y=0),
                    length=3,
                    shout="",
                    squad="",
                    customizations=models.Customization(
                        color="#0000ff", head="pixel", tail="pixel"
                    ),
                ),
                models.Battlesnake(
                    id="gs_GKwVgGSFRXxJMPPHYkPGKRXJ",
                    name="Midgaardsorm",
                    health=97,
                    body=[
                        models.Position(x=3, y=4),
                        models.Position(x=2, y=4),
                        models.Position(x=1, y=4),
                        models.Position(x=0, y=4),
                    ],
                    latency="30",
                    head=models.Position(x=3, y=4),
                    length=4,
                    shout="",
                    squad="",
                    customizations=models.Customization(
                        color="#84e0c7", head="fang", tail="round-bum"
                    ),
                ),
                models.Battlesnake(
                    id="gs_QrYm46KQ6Yc9vqQKG3bdSKQD",
                    name="First Battlesnake",
                    health=97,
                    body=[
                        models.Position(x=6, y=7),
                        models.Position(x=6, y=8),
                        models.Position(x=6, y=9),
                        models.Position(x=6, y=10),
                    ],
                    latency="93",
                    head=models.Position(x=6, y=7),
                    length=4,
                    shout="",
                    squad="",
                    customizations=models.Customization(
                        color="#b62b2b", head="default", tail="default"
                    ),
                ),
                models.Battlesnake(
                    id="gs_t9SJgdBJW4gGcFbBgqkvVRS9",
                    name="Hungry Snake",
                    health=97,
                    body=[
                        models.Position(x=7, y=6),
                        models.Position(x=8, y=6),
                        models.Position(x=9, y=6),
                        models.Position(x=10, y=6),
                    ],
                    latency="43",
                    head=models.Position(x=7, y=6),
                    length=4,
                    shout="",
                    squad="",
                    customizations=models.Customization(
                        color="#11baa1", head="duck", tail="do-sammy"
                    ),
                ),
            ],
        ),
        you=models.Battlesnake(
            id="gs_QrYm46KQ6Yc9vqQKG3bdSKQD",
            name="First Battlesnake",
            health=97,
            body=[
                models.Position(x=6, y=7),
                models.Position(x=6, y=8),
                models.Position(x=6, y=9),
                models.Position(x=6, y=10),
            ],
            latency="93",
            head=models.Position(x=6, y=7),
            length=4,
            shout="",
            squad="",
            customizations=models.Customization(
                color="#b62b2b", head="default", tail="default"
            ),
        ),
    )


def test_move_api(game_state):
    result = move.make_move(game_state)
    assert result == models.MoveEnum.LEFT
