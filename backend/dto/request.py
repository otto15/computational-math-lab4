from pydantic import BaseModel


class PointTo(BaseModel):
    x: float
    y: float


class ApproxRequestTo(BaseModel):
    points: list[PointTo]
