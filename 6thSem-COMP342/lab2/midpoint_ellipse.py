from plot import *


def get_input():
    """Get input for ellipse's centre and rx_ry_axes"""

    global centre, rx_ry_axes
    centre = input("Enter centre of ellipse [format-> `xc,yc`]: ")
    rx_ry_axes = input("Enter rx_ry_axes of ellipse [format-> `rx,ry`]: ")

    centre = [int(point) for point in centre.split(",")]
    rx_ry_axes = [int(length) for length in rx_ry_axes.split(",")]


def _get_symmetric_points(x: int, y: int) -> list:
    """
    Get Symmetric points for ellipse
    Note: a point has 3 other symmetric points in ellipse

    Returns a list with 4 way symmetry ellipse symmetric points
    """
    return [[x, y], [-x, y], [x, -y], [-x, -y]]


def _adjust_points_to_centre(x_y: list, centre: list) -> list:
    """
    Adds `centre` values to coordinates in list `x_y`

    using `map` to return values after manipulating it by first argument
    for all elements of second argument.
    It is similar to for element in second arg do as suggested first arg

    Returns list with centre adjusted coordinates
    """

    return list(map(lambda arr: [(arr[0] + centre[0]), (arr[1] + centre[1])], x_y))


def midpoint_ellipse(center: list = None, rx_ry_axes: list = None):
    """
    Calculate ellipse coordinates based on given centre and axes rx_ry_axes
    """

    if not (center and rx_ry_axes):
        get_input()

    rx, ry = rx_ry_axes[0], rx_ry_axes[1]

    x, y = 0, ry  # start from 0,ry
    X_Y = []  # list for storing coordinates

    dx = 2 * ry**2 * x
    dy = 2 * rx**2 * y

    #
    ## REGION 1

    decision_parameter1 = (ry**2) + (0.25 * rx**2) - (rx**2 * ry)
    while dx < dy:
        X_Y.append([x, y])
        if decision_parameter1 < 0:
            x += 1
            dx = 2 * ry**2 * x
            decision_parameter1 += 2 * ry**2 * x + ry**2

        else:
            x += 1
            y -= 1
            dx = 2 * ry**2 * x
            dy = 2 * rx**2 * y
            decision_parameter1 += (2 * ry**2 * x) - (2 * rx**2 * y) + (ry**2)

    #
    ## REGION 2

    decision_parameter2 = (
        (ry**2 * (x + 0.5) ** 2) + (rx**2 * (y - 1) ** 2) - (rx**2 * ry**2)
    )

    while y > 0:
        X_Y.append([x, y])
        if decision_parameter2 > 0:
            y -= 1
            dy = 2 * rx**2 * y
            decision_parameter2 += rx**2 - (2 * rx**2 * y)

        else:
            y -= 1
            x += 1
            dx = 2 * ry**2 * x
            dy = 2 * rx**2 * y
            decision_parameter2 += (2 * ry**2 * x) - (2 * rx**2 * y) + (rx**2)

    X_Y.append([x, y])

    final_X_Y = []
    for point in X_Y:
        final_X_Y += _adjust_points_to_centre(
            _get_symmetric_points(point[0], point[1]), center
        )

    return final_X_Y


if __name__ == "__main__":
    Points = midpoint_ellipse([0, -50], [250, 312])
    startGlutPlot("Ellipse drawing using Midpoint Algorithm", Points, "red")
