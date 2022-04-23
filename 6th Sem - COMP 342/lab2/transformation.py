import math
import numpy as np
from plot import *


class Transformation(object):

    vertices = None
    homogeneous_vertices = None
    transformation_matrix = None
    vertex_matrix = None

    def __init__(self, vertices: list) -> list:
        self.vertices = np.array(vertices)
        self.homogeneous_vertices = np.array([vertex + [1] for vertex in vertices])
        self.vertex_matrix = np.array(
            [list(row) for row in zip(*self.homogeneous_vertices)]
        )

    def _apply_transformation(self):
        transformed_vertices = []
        transformed_vertices = self.transformation_matrix.dot(self.vertex_matrix)
        return [list(row[:2]) for row in list(zip(*transformed_vertices))]

    def translate2D(self, tx, ty):
        self.transformation_matrix = np.array(
            [
                [1, 0, tx],
                [0, 1, ty],
                [0, 0, 1],
            ]
        )
        return self._apply_transformation()

    def scale2D(self, sx, sy):
        self.transformation_matrix = np.array(
            [
                [sx, 0, 0],
                [0, sy, 0],
                [0, 0, 1],
            ]
        )
        return self._apply_transformation()

    def rotation2D(self, angle_in_degrees):
        theta = math.radians(angle_in_degrees)
        self.transformation_matrix = np.array(
            [
                [math.cos(theta), -math.sin(theta), 0],
                [math.sin(theta), math.cos(theta), 0],
                [0, 0, 1],
            ]
        )
        return self._apply_transformation()

    def reflection2D(self, axis):
        if axis.upper() == "X":
            self.transformation_matrix = np.array(
                [
                    [1, 0, 0],
                    [0, -1, 0],
                    [0, 0, 1],
                ]
            )
        elif axis.upper() == "Y":
            self.transformation_matrix = np.array(
                [
                    [-1, 0, 0],
                    [0, 1, 0],
                    [0, 0, 1],
                ]
            )
        elif axis.upper() == "Y=X":
            self.transformation_matrix = np.array(
                [
                    [0, 1, 0],
                    [1, 0, 0],
                    [0, 0, 1],
                ]
            )
        elif axis.upper() == "Y=-X":
            self.transformation_matrix = np.array(
                [
                    [0, -1, 0],
                    [-1, 0, 0],
                    [0, 0, 1],
                ]
            )
        elif axis.upper() == "ORIGIN":
            self.transformation_matrix = np.array(
                [
                    [-1, 0, 0],
                    [0, -1, 0],
                    [0, 0, 1],
                ]
            )

        return self._apply_transformation()

    def shear2D(self, sh, axis):

        if axis.upper() == "X":
            shx, shy = sh, 0
        elif axis.upper() == "Y":
            shx, shy = 0, sh
        else:
            shx, shy = 0, 0

        self.transformation_matrix = np.array(
            [
                [1, shx, 0],
                [shy, 1, 0],
                [0, 0, 1],
            ]
        )
        return self._apply_transformation()


if __name__ == "__main__":
    polygon = [
        [120, 60],
        [180, 120],
        [140, 120],
        [140, 180],
        [100, 180],
        [100, 120],
        [60, 120],
    ]
    T = Transformation(polygon)
    figures = [
        # polygon,
        # T.translate2D(100, 100),
        # T.scale2D(2, 2),
        # T.rotation2D(90),
        # T.rotation2D(45),
        # T.rotation2D(-45),
        # T.rotation2D(-95),
        # T.reflection2D("x"),
        # T.reflection2D("y"),
        # T.reflection2D("y=-x"),
        # T.shear2D(0.5, "y"),
        # T.shear2D(0.5, "x"),
        [[-60, -300], [60, -300], [30, 60], [0, 100], [-30, 60]],
        [[-420, 100], [0, 100], [-90, 120], [-90, 140]],
    ]

    startPolygonPlot("Transformation: Shear", figures)
    print("done")
