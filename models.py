from pydantic import BaseModel


class Game(BaseModel):
    id: str
    ruleset: dict
    map: str
    timeout: int
    source: str


class Position(BaseModel):
    x: int
    y: int


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
    customizations: dict


class Board(BaseModel):
    height: int
    width: int
    food: list[Position]
    hazards: list[Position]
    snakes: list[Battlesnake]


class Body(BaseModel):
    game: Game
    turn: int
    board: Board
    you: Battlesnake
