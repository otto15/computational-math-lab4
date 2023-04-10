from math import log, exp

from domain.approx import ApproxData, ApproxResult
from approximation.strategies import linear_approximation


def approx(data: ApproxData) -> ApproxResult:
    ys = data.y

    if not all(y > 0 for y in ys):
        return ApproxResult(lambda x: 0, [], 'exp')

    ln_ys = [log(y) for y in ys]

    result = linear_approximation.approx(ApproxData(data.x, ln_ys))
    coefficients = result.coefficients
    a = exp(coefficients[0])
    b = coefficients[1]

    return ApproxResult(lambda x: a * exp(b * x), [b, a], "exp")
