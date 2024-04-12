from pydantic import BaseModel
from enum import Enum


class Brand(str, Enum):
    nitro = "Nitro"
    saloman = "Saloman"
    burton = "Burton"


class Snowboard(BaseModel):
    length: int
    color: str
    has_bindings: bool
    brand: str
