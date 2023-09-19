from pydantic import BaseModel


class Game(BaseModel):
    id: str
    ruleset: dict
    map: str
    timeout: int
    source: str


class Board(BaseModel):
    height: int
    width: int
    food: list
    hazards: list
    snakes: list


class Battlesnake(BaseModel):
    id: str
    name: str
    health: int
    body: list
    latency: str
    head: dict
    length: int
    shout: str
    squad: str
    customizations: dict


class Body(BaseModel):
    game: Game
    turn: int
    board: Board
    you: Battlesnake
