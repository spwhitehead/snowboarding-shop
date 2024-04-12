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


@app.put("/snowboards/{board_id}")
async def update_snowboard(board_id: int, updated_snowboard: Snowboard) -> None:
    for i, board in enumerate(snowboards):
        if board.id == board_id:
            board[i] = updated_snowboard
            return "Snowboard updated successfully"


@app.delete("/snowboards/{board_id}")
async def delete_snowboard(board_id: int) -> None:
    for i, board in enumerate(snowboards):
        if board.id == board_id:
            snowboards.pop(i)
            return "Item deleted successfully"
