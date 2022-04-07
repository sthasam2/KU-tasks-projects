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

    if not (x1 and x2 and y1 and y2):
        get_input()

    if x2 > x1:
        dx, dy = (x2 - x1), (y2 - y1)  # getting differences
        x, y = x1, y1  # making starting points
    else:
        dx, dy = (x1 - x2), (y1 - y2)
        x, y = x2, y2

    # setting decision parameter parameters based on slope
    if abs(dx) > abs(dy):  # slope < 1
        c1, c2 = (2 * dy), (2 * (dy - dx))
        p = c1 - dx

        for _ in range(abs(dx)):
            X_Y.append([x, y])

            # Calculating decision parameters
            if p < 0:
                p += c1
            else:
                p += c2
                y += 1
            x += 1
    else:  # slope => 1
        c1, c2 = 2 * abs(dx), 2 * (abs(dx) - abs(dy))
        p = c1 - dy

        for _ in range(abs(dy)):
            X_Y.append([x, y])

            # Calculating decision parameters
            if p < 0:
                p += c1
            else:
                p += c2
                x += 1
            y += 1

    return X_Y


if __name__ == "__main__":
    Points = BLA(69, 69, 420, 420)
    plotInGlut("Line Drawing Using BLA", Points, "blue")
