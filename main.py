from fastapi import FastAPI

from models import Body
from move import make_move

app = FastAPI()


@app.get("/")
async def root():
    return {
        "apiversion": "1",
        "author": "codeguru42",
        "color": "#B62B2B",
        "head": "default",
        "tail": "default",
        "version": "0.0.1-beta",
    }


@app.post("/start")
async def start():
    return {"message": "starting"}


@app.post("/move")
async def move(body: Body):
    print(body)
    return {"move": make_move()}


@app.post("/end")
async def end():
    return {"message": "ending"}
