from math import pi, sin, cos
from plot import *
from BLA import BLA
from DDA import DDA
from midpoint_circle import midpoint_circle


def get_input():
    """Get a list of items to plot in pie chart"""

    items = input("Enter a list of items to plot in chart [format-> 100, 2000, 450]: ")
    items = [int(item) for item in items.split(",")]


def pie_chart(items: list) -> list:
    """ """

    CENTRE = [512, 384]
    RADIUS = 300
    _2PI = 2 * pi

    if not items:
        get_input()

    total_value = sum(items)
    sector_angles = [0]
    sector_end_points = []

    for i in range(0, len(items)):

        previous_angle = sector_angles[i]
        current_angle = previous_angle + (_2PI * items[i] / total_value)
        sector_angles.append(current_angle)

        current_end_point = [
            round(CENTRE[0] + RADIUS * sin(current_angle)),
            round(CENTRE[1] + RADIUS * cos(current_angle)),
        ]
        sector_end_points.append(current_end_point)

    circle_coordinates = [
        midpoint_circle(
            list(map(lambda a: int(a), CENTRE)),
            int(RADIUS),
        )
    ]
    sector_line_coordinates = [
        DDA(CENTRE[0], CENTRE[1], ep[0], ep[1]) for ep in sector_end_points
    ]

    all_coordinates = circle_coordinates + sector_line_coordinates

    # drawing
    plotMultipleInGlut(
        "Pie Chart",
        all_coordinates,
    )


if __name__ == "__main__":
    pie_chart([100, 200, 400, 800, 1600])
    # pie_chart([100, 100, 100, 100, 100])
