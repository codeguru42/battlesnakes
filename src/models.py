from enum import StrEnum

from pydantic import BaseModel


class MetaData(BaseModel):
    apiversion: str
    author: str
    color: str
    head: str
    tail: str
    version: str


class RoyaleSettings(BaseModel):
    shrinkEveryNTurns: int


class SquadSettings(BaseModel):
    allowBodyCollisions: bool
    sharedElimination: bool
    sharedHealth: bool
    sharedLength: bool


class RulesetSettings(BaseModel):
    foodSpawnChance: int
    minimumFood: int
    hazardDamagePerTurn: int
    royale: RoyaleSettings
    squad: SquadSettings


class Ruleset(BaseModel):
    name: str
    version: str
    settings: RulesetSettings


class Game(BaseModel):
    id: str
    ruleset: Ruleset
    map: str
    timeout: int
    source: str


class Position(BaseModel):
    x: int
    y: int

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __add__(self, other):
        if isinstance(other, MoveEnum):
            return Position(
                x=self.x + MoveEnum(other).delta().x,
                y=self.y + MoveEnum(other).delta().y,
            )


class Customization(BaseModel):
    color: str
    head: str
    tail: str


class Battlesnake(BaseModel):
    id: str
    name: str
    health: int
    body: list[Position]
    latency: str
    head: Position
    length: int
    shout: str
    squad: str
    customizations: Customization

    def __hash__(self):
        return hash(id)


class Board(BaseModel):
    height: int
    width: int
    food: list[Position]
    hazards: list[Position]
    snakes: list[Battlesnake]


class GameState(BaseModel):
    game: Game
    turn: int
    board: Board
    you: Battlesnake


class MoveEnum(StrEnum):
    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"

    def delta(self):
        match self:
            case MoveEnum.UP:
                return Position(x=0, y=1)
            case MoveEnum.DOWN:
                return Position(x=0, y=-1)
            case MoveEnum.LEFT:
                return Position(x=-1, y=0)
            case MoveEnum.RIGHT:
                return Position(x=1, y=0)


class Move(BaseModel):
    move: MoveEnum


class Message(BaseModel):
    message: str
