from typing import Callable


class ApproxData:
    x: list[float]
    y: list[float]

    def __init__(self, x, y):
        self.x = x
        self.y = y


class ApproxResult:
    strategy_name: str
    phi: Callable[[float], float]
    coefficients: list[float]

    def __init__(self, phi, coefficients, strategy_name):
        self.phi = phi
        self.coefficients = coefficients
        self.strategy_name = strategy_name
