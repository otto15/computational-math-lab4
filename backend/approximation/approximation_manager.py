from dto.response import ApproxResultTo
from dto.request import ApproxRequestTo
from domain.approx import ApproxData, ApproxResult
from approximation.strategies import exp_approximation, log_approximation, power_approximation, \
    linear_approximation, cubic_approximation, square_approximation
from math import sqrt


def transform_to_approx_data(to: ApproxRequestTo) -> ApproxData:
    xs = [point.x for point in to.points]
    ys = [point.y for point in to.points]
    data = ApproxData(xs, ys)
    return data


def standard_deviation(approx_result: ApproxResult, xs: list[float], ys: list[float]) -> float:
    phi = approx_result.phi
    res = sqrt(sum([(phi(x) - y) ** 2 for x, y in zip(xs, ys)]) / len(xs))
    return res


def find_closest(results: list[ApproxResult], xs: list[float], ys: list[float]) -> str:
    results = list(filter(lambda result: len(result.coefficients) > 0, results))
    min_deviation = min([standard_deviation(result, xs, ys) for result in results])
    return list(filter(lambda result: min_deviation == standard_deviation(result, xs, ys), results))[0].strategy_name


def approximate(approx_to: ApproxRequestTo) -> ApproxResultTo:
    data = transform_to_approx_data(approx_to)

    cubic = cubic_approximation.approx(data)
    exp = exp_approximation.approx(data)
    linear = linear_approximation.approx(data)
    log = log_approximation.approx(data)
    power = power_approximation.approx(data)
    square = square_approximation.approx(data)

    result_list = [cubic, exp, linear, log, power, square]

    return ApproxResultTo(
        chosen=find_closest(result_list, data.x, data.y),
        log=log.coefficients,
        cubic=cubic.coefficients,
        exp=exp.coefficients,
        linear=linear.coefficients,
        power=power.coefficients,
        square=square.coefficients
    )
