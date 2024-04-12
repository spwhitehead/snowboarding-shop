import json

from fastapi import FastAPI, HTTPException
from typing import Dict

from models import Snowboard, Brand

app = FastAPI()


with open("snowboards.json", "r") as f:
    snowboard_list = json.load(f)

snowboards: Dict[int, Snowboard] = {}


def load_json_data():
    try:
        with open("snowboards.json", "r") as f:
            snowboard_list = json.load(f)
        for snowboard_data in snowboard_list:
            snowboard = Snowboard.model_validate(snowboard_data)
            snowboards[snowboard.id] = snowboard
    except Exception as e:
        print(f"Failed to load snowboards from JSON: {e}")


load_json_data()


@app.get("/snowboards")
async def read_snowboard():
    return list(snowboards.values())


@app.post("/snowboards/", response_model=Snowboard)
async def create_snowboard(snowboard: Snowboard):
    if snowboard.id in snowboards:
        raise HTTPException(status_code=400, detail="Snowboard already exists")
    snowboards[snowboard.id] = snowboard
    return snowboard


@app.put("/snowboards/{snowboard_id}", response_model=Snowboard)
def update_snowboard(snowboard_id: int, snowboard: Snowboard):
    if snowboard_id not in snowboards:
        raise HTTPException(status_code=404, detail="Snowboard not found")
    snowboards[snowboard_id] = snowboard
    return snowboard


@app.delete("/snowboards/{snowboard_id}")
def delete_snowboard(snowboard_id: int):
    if snowboard_id not in snowboards:
        raise HTTPException(status_code=404, detail="Snowboard not found")
    del snowboards[snowboard_id]
    return {"ok": True}
