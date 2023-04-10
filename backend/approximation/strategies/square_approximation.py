from domain.approx import ApproxResult, ApproxData
from matrix import gauss


def approx(data: ApproxData) -> ApproxResult:
    xs = data.x
    ys = data.y

    x_sum = sum(xs)
    y_sum = sum(ys)

    square_x_sum = sum([x ** 2 for x in xs])
    cube_x_sum = sum([x ** 3 for x in xs])
    fourth_x_sum = sum([x ** 4 for x in xs])

    xy_sum = sum([x * y for x, y in zip(xs, ys)])
    square_x_y_sum = sum([(x ** 2) * y for x, y in zip(xs, ys)])

    matrix = [
        [len(xs), x_sum, square_x_sum, y_sum],
        [x_sum, square_x_sum, cube_x_sum, xy_sum],
        [square_x_sum, cube_x_sum, fourth_x_sum, square_x_y_sum]
    ]

    solution = gauss.count_result(matrix)

    phi = lambda x: solution[0] + solution[1] * x + solution[2] * (x ** 2)

    return ApproxResult(phi, solution, "square")
