from pydantic import BaseModel


class ApproxResultTo(BaseModel):
    chosen: str
    log: list[float]
    cubic: list[float]
    exp: list[float]
    linear: list[float]
    power: list[float]
    square: list[float]
