from domain.approx import ApproxData, ApproxResult
from matrix import gauss


def approx(data: ApproxData) -> ApproxResult:
    xs, ys, n = data.x, data.y, len(data.x)

    x_sum, y_sum = sum(xs), sum(ys)
    square_x_sum = sum([x ** 2 for x in xs])
    xy_sum = sum([x * y for x, y in zip(xs, ys)])

    matrix = [
        [n, x_sum, y_sum],
        [x_sum, square_x_sum, xy_sum]
    ]

    solution = gauss.count_result(matrix)

    phi = lambda x: solution[0] + solution[1] * x

    return ApproxResult(phi, solution, "linear")
