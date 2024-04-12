import json

from fastapi import FastAPI
from models import Snowboard, Brand

app = FastAPI()


with open("snowboards.json", "r") as f:
    snowboard_list = json.load(f)

snowboards: list[Snowboard] = []

for board in snowboard_list:
    snowboards.append(Snowboard(**board))


@app.get("/snowboards")
async def list_snowboards() -> list[Snowboard]:
    return snowboards


@app.post("/snowboards")
async def add_snowboard(board: Snowboard) -> None:
    snowboards.append(board)


@app.put
