from plot import *


def get_input():
    """Get input for circle's centre and radius"""

    global centre, radius
    centre = input("Enter centre of circle [format-> `xc,yc`]: ")
    radius = input("Enter radius of circle [format-> `r`]: ")

    centre = [int(point) for point in centre.split(",")]
    radius = int(radius)


def _get_symmetric_points(x: int, y: int) -> list:
    """
    Get Symmetric points for circle
    Note: a point has 7 other symmetric points in circle

    Returns a list with 8 circle symmetric points
    """
    return [[x, y], [y, x], [-x, y], [y, -x], [x, -y], [-y, x], [-x, -y], [-y, -x]]


def _adjust_points_to_centre(x_y: list, centre: list) -> list:
    """
    Adds `centre` values to coordinates in list `x_y`

    using `map` to return values after manipulating it by first argument
    for all elements of second argument.
    It is similar to for element in second arg do as suggested first arg

    Returns list with centre adjusted coordinates
    """

    return list(map(lambda arr: [(arr[0] + centre[0]), (arr[1] + centre[1])], x_y))


def midpoint_circle(center: list = None, radius: int = None):
    """
    Calculate circle coordinates based on given centre and radius
    """

    if not (center and radius):
        get_input()

    x, y = 0, radius  # start from 0,r
    X_Y = []  # list for storing coordinates

    p = 1 - radius  # p0 initial decision parameter

    while x < y:
        X_Y += _adjust_points_to_centre(
            _get_symmetric_points(x, y),
            center,
        )  # add centre adjusted symmetrical points to list

        x += 1  # unit increment of x

        # calculating decision paramater based on previous decision parameter
        if p < 0:
            p += 2 * x + 1
        else:
            p += 2 * (x - y) + 1
            y -= 1

    return X_Y


if __name__ == "__main__":
    Points = midpoint_circle([0, 0], 200)
    startGlutPlot("Circle drawing using Midpoint Algorithm", Points, "green")
