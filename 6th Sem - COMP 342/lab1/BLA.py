from plot import *


def get_input():
    """
    Get input for line's start and end coordinates
    """
    global x1, y1, x2, y2
    start = input("Enter start points x1, y1: ")
    end = input("Enter enp points x2, y2 : ")

    start = [int(point) for point in start.split(",")]
    end = [int(point) for point in end.split(",")]

    x1, y1 = start[0], start[1]
    x2, y2 = end[0], end[1]


def BLA(x1: int = None, y1: int = None, x2: int = None, y2: int = None) -> list:
    """
    Calculate line coordinates based on given start and end coordinates
    """

    X_Y = []

    if x1 == y1 == x2 == y2 == None:
        get_input()

    dx, dy = (x2 - x1), (y2 - y1)  # getting differences

    x_inc = 1 if dx > 0 else -1
    y_inc = 1 if dy > 0 else -1
    x, y = x1, y1

    # setting decision parameter parameters based on slope
    if abs(dy) < abs(dx):  # slope < 1
        # making starting points

        p = 2 * abs(dy) - abs(dx)
        c1 = 2 * abs(dy)
        c2 = 2 * (abs(dy) - abs(dx))

        for _ in range(abs(dx)):
            X_Y.append([x, y])

            if p < 0:
                p += c1
            else:
                p += c2
                y += y_inc
            x += x_inc
    else:  # slope => 1

        p = 2 * abs(dx) - abs(dy)
        c1 = 2 * abs(dx)
        c2 = 2 * (abs(dx) - abs(dy))

        for _ in range(abs(dy)):
            X_Y.append([x, y])
            if p < 0:
                p += c1
            else:
                p += c2
                x += x_inc
            y += y_inc

    return X_Y


def rand_4_ints():
    return (random.randrange(-540, 540) for _ in range(4))


if __name__ == "__main__":
    # Points = [BLA(69, 420, -19, -520)]
    # Points.append(BLA(-102, -180, 202, 480))
    # Points.append(BLA(213, 501, -313, -301))
    # Points.append(BLA(-185, 333, 485, -233))

    Points = [BLA(*rand_4_ints())]
    Points.append(BLA(*rand_4_ints()))
    Points.append(BLA(*rand_4_ints()))
    Points.append(BLA(*rand_4_ints()))

    startGlutMultipleItemPlot("Line Drawing Using BLA", Points)
