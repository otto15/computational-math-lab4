from math import log

from domain.approx import ApproxData, ApproxResult
from approximation.strategies import linear_approximation


def approx(data: ApproxData) -> ApproxResult:
    if not all(x > 0 for x in data.x):
        return ApproxResult(lambda x: 0, [], 'log')

    ln_xs = [log(x) for x in data.x]

    coefficients = linear_approximation.approx(ApproxData(ln_xs, data.y)).coefficients

    return ApproxResult(lambda x: coefficients[0] + log(x) * coefficients[1], coefficients, "log")
