from plot import *


def get_input():
    """Get input for line's start and end coordinates"""

    global x1, y1, x2, y2
    start = input("Enter start points x1, y1: ")
    end = input("Enter end points x2, y2 : ")

    start = [int(point) for point in start.split(",")]
    end = [int(point) for point in end.split(",")]

    x1, y1 = start[0], start[1]
    x2, y2 = end[0], end[1]


def DDA(x1=None, y1=None, x2=None, y2=None):
    """
    Calculate line coordinates based on given start and end coordinates
    """

    if not (x1 and y1 and x2 and y2):
        get_input()

    dx, dy = (x2 - x1), (y2 - y1)
    step = abs(dx) if abs(dx) > abs(dy) else abs(dy)
    x_inc, y_inc = (dx / step), (dy / step)

    # start points
    x, y = [x1], [y1]
    i = 0
    while i <= step:
        x.append(x[i] + x_inc)
        y.append(y[i] + y_inc)
        i += 1

    return [[round(x[i]), round(y[i])] for i in range(len(x) - 1)]


if __name__ == "__main__":
    Points = DDA(2, 3, 410, 420)
    plotInGlut("Line Drawing Using DDA", Points, "red")
