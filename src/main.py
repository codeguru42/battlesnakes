from fastapi import FastAPI

from models import GameState, Move, MetaData, Message
from move import make_move

app = FastAPI()


@app.get("/")
async def root() -> MetaData:
    return MetaData(
        apiversion="1",
        author="codeguru42",
        color="#B62B2B",
        head="default",
        tail="default",
        version="0.0.1-beta",
    )


@app.post("/start")
async def start() -> Message:
    return Message(message="starting")


@app.post("/move")
async def move(state: GameState) -> Move:
    print(repr(state))
    m = make_move(state)
    print(m)
    return Move(move=m)


@app.post("/end")
async def end() -> Message:
    return Message(message="ending")
