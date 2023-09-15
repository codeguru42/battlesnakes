from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {
      "apiversion": "1",
      "author": "codeguru42",
      "color": "#B62B2B",
      "head": "default",
      "tail": "default",
      "version": "0.0.1-beta"
    }


@app.post("/start")
async def start():
    return {
        "message": "starting"
    }
