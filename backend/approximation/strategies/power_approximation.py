from math import log, exp

from domain.approx import ApproxData, ApproxResult
from approximation.strategies import linear_approximation


def approx(data: ApproxData) -> ApproxResult:
    xs, ys = data.x, data.y

    if not all(x > 0 and y > 0 for x, y in zip(xs, ys)):
        return ApproxResult(lambda x: 0, [], 'power')

    ln_xs = [log(x) for x in xs]
    ln_ys = [log(y) for y in ys]

    coefficients = linear_approximation.approx(ApproxData(ln_xs, ln_ys)).coefficients
    a = exp(coefficients[0])
    b = coefficients[1]

    return ApproxResult(lambda x: a * pow(x, b), [b, a], "power")
