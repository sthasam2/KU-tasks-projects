from time import sleep
from utils import clockwiseangle_and_distance

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


class SutherlandHodgemanPolygonClipping:
    """ """

    # Defining XW_MAX, YW_MAX and XW_MIN, YW_MIN for viewport rectangle
    XW_MAX = None
    YW_MAX = None
    XW_MIN = None
    YW_MIN = None

    # boundaries
    LEFT = 0
    RIGHT = 1
    BOTTOM = 2
    TOP = 3

    # case
    IN_TO_IN = 0
    IN_TO_OUT = 1
    OUT_TO_IN = 2
    OUT_TO_OUT = 3

    original_polygon_vertices = None
    clipped_polygon_vertices = []

    # display display_step i.e.
    # 0: original line -> 1: window for clipping -> 2: clipped with window -> 3: clipped
    display_step = 0

    width, height = 1900, 1000
    window_color = (0.4, 0.4, 0.0, 1.0)
    original_polygon_color = (0.90, 0.20, 0.0, 0.5)
    clipped_polygon_color = (0.20, 0.90, 0.0, 0.5)

    def __init__(self, window_region: list, polygon_vertices: list) -> None:
        """
        window_region: <list>[self.XW_MAX, self.YW_MAX, self.XW_MIN, self.YW_MIN]
        polygon_vertices: <list>[(x1, y1), (x2, y2), (x3, y3), ...]
        """
        assert (
            len(window_region) == 4
        ), "Window region must include [self.XW_MAX, self.YW_MAX, self.XW_MIN, self.YW_MIN]"
        assert (
            len(polygon_vertices) > 2
        ), "Ploygons must have equal to or more than 3 vertices"

        (
            self.XW_MAX,
            self.YW_MAX,
            self.XW_MIN,
            self.YW_MIN,
        ) = window_region
        self.original_polygon_vertices = polygon_vertices

    def _window_vertices(self):
        """
        Returns tuple: TL[x,y], TR[x,y], BR[x,y], BL[x,y]

        Note: T: Top, L: Left, R: Right, B: Bottom
        """
        return (
            [self.XW_MIN, self.YW_MAX],
            [self.XW_MAX, self.YW_MAX],
            [self.XW_MAX, self.YW_MIN],
            [self.XW_MIN, self.YW_MIN],
        )

    def _window_lines(self):
        """
        Returns tuple:
        ((TL(x,y), TR(x,y)),
        ((TR(x,y), BR(x,y)),
        ((BR(x,y), BL(x,y)),
        ((BR(x,y), BL(x,y))

        Note: T: Top, L: Left, R: Right, B: Bottom
        """

        return (
            (
                (self.XW_MIN, self.YW_MAX),
                (self.XW_MAX, self.YW_MAX),
            ),
            (
                (self.XW_MAX, self.YW_MAX),
                (self.XW_MAX, self.YW_MIN),
            ),
            (
                (self.XW_MAX, self.YW_MIN),
                (self.XW_MIN, self.YW_MIN),
            ),
            (
                (self.XW_MIN, self.YW_MIN),
                (self.XW_MIN, self.YW_MAX),
            ),
        )

    def _original_polygon_vertices(self):
        """Returns list: (x1,y1), (x2,y2), ..."""

        return self.original_polygon_vertices

    def _clipped_polygon_vertices(self):
        """Returns tuple: <Clipped Start>[x,y], <Clipped End>[x,y]"""

        if self.clipped_polygon_vertices == None:
            self.clipped_polygon_vertices = self.liang_barsky_clip()
        return self.clipped_polygon_vertices

    def _carry_out_calculations(self):
        self._original_polygon_vertices()
        self._clipped_polygon_vertices()

    def _get_case(self, boundary, p1, p2):

        (x1, y1) = p1  # tuple unpacking
        (x2, y2) = p2
        if boundary == self.LEFT:
            if x1 >= self.XW_MIN and x2 >= self.XW_MIN:
                return self.IN_TO_IN
            elif x1 >= self.XW_MIN:
                return self.IN_TO_OUT
            elif x2 >= self.XW_MIN:
                return self.OUT_TO_IN
            else:
                return self.OUT_TO_OUT
        elif boundary == self.RIGHT:
            if x1 <= self.XW_MAX and x2 <= self.XW_MAX:
                return self.IN_TO_IN
            elif x1 <= self.XW_MAX:
                return self.IN_TO_OUT
            elif x2 <= self.XW_MAX:
                return self.OUT_TO_IN
            else:
                return self.OUT_TO_OUT
        elif boundary == self.BOTTOM:
            if y1 >= self.YW_MIN and y2 >= self.YW_MIN:
                return self.IN_TO_IN
            elif y1 >= self.YW_MIN:
                return self.IN_TO_OUT
            elif y2 >= self.YW_MIN:
                return self.OUT_TO_IN
            else:
                return self.OUT_TO_OUT
        elif boundary == self.TOP:
            if y1 <= self.YW_MAX and y2 <= self.YW_MAX:
                return self.IN_TO_IN
            elif y1 <= self.YW_MAX:
                return self.IN_TO_OUT
            elif y2 <= self.YW_MAX:
                return self.OUT_TO_IN
            else:
                return self.OUT_TO_OUT

    def _find_intersection(self, boundary, p1, p2):
        (x1, y1) = p1
        (x2, y2) = p2
        m = 0
        if x1 != x2:
            m = (y2 - y1) / (x2 - x1)
        if boundary == self.LEFT:
            return (self.XW_MIN, y1 + m * (self.XW_MIN - x1))
        elif boundary == self.RIGHT:
            return (self.XW_MAX, y1 + m * (self.XW_MAX - x1))
        elif boundary == self.BOTTOM:
            if x1 == x2:
                return (x1, self.YW_MIN)
            else:
                return (x1 + (self.YW_MIN - y1) / m, self.YW_MIN)
        elif boundary == self.TOP:
            if x1 == x2:
                return (x1, self.YW_MAX)
            else:
                return (x1 + (self.YW_MAX - y1) / m, self.YW_MAX)

    def clip_polygon(self):
        vertices = self.original_polygon_vertices

        new_vertices = []
        for boundary in range(4):

            for i in range(len(vertices)):
                p1 = vertices[i]
                p2 = vertices[(i + 1) % (len(vertices))]

                case = self._get_case(boundary, p1, p2)

                if (case == self.IN_TO_IN) & (p2 not in new_vertices):
                    new_vertices.append(p2)
                elif case == self.IN_TO_OUT:
                    p = self._find_intersection(boundary, p1, p2)
                    new_vertices.append(p)
                elif case == self.OUT_TO_IN:
                    p = self._find_intersection(boundary, p1, p2)
                    new_vertices.append(p)
                    new_vertices.append(p2)

        for index, vertex in enumerate(new_vertices):
            if not (
                (self.XW_MIN <= vertex[0] <= self.XW_MAX)
                & (self.YW_MIN <= vertex[1] <= self.YW_MAX)
            ):
                new_vertices.pop(index)

        # sort vertices for displaying in opengl
        new_vertices = sorted(new_vertices, key=clockwiseangle_and_distance)
        self.clipped_polygon_vertices = new_vertices
        return self.clipped_polygon_vertices

    def _draw_line(self, ends):
        # ends = self._window_lines()
        if ends is not None:
            glPointSize(10.0)
            # for end in ends:
            for (x, y) in ends:
                glBegin(GL_LINES)
                glVertex2f(x, y)
                glEnd()

    def _draw_window_lines(self):
        ends = self._window_lines()
        if ends is not None:
            glPointSize(10.0)
            for end in ends:
                glBegin(GL_LINES)
                for (x, y) in end:
                    glVertex2f(x, y)
                glEnd()

    def _draw_polygon(self, vertices):
        glPointSize(5.0)
        glBegin(GL_POLYGON)
        for (x, y) in vertices:
            glVertex2f(x, y)
        glEnd()

    def draw_polygon(self, vertices):
        for i in range(len(vertices)):
            (x1, y1) = vertices[i]
            (x2, y2) = vertices[(i + 1) % len(vertices)]
            glBegin(GL_LINES)
            glVertex2f(x1, y1)
            glVertex2f(x2, y2)
            glEnd()

    def _draw_clipping(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        if self.display_step == 0:
            glColor4f(*self.original_polygon_color)
            self._draw_polygon(self.original_polygon_vertices)
            self.display_step = 1

        elif self.display_step == 1:
            glColor4f(*self.window_color)
            self._draw_window_lines()
            glColor4f(*self.original_polygon_color)
            self._draw_polygon(self.original_polygon_vertices)
            self.display_step = 2

        elif self.display_step == 2:
            glColor4f(*self.window_color)
            self._draw_window_lines()
            glColor4f(*self.clipped_polygon_color)
            self._draw_polygon(self.clipped_polygon_vertices)
            self.display_step = 3

        elif self.display_step == 3:
            glColor4f(*self.clipped_polygon_color)
            self._draw_polygon(self.clipped_polygon_vertices)
            self.display_step = 0

        sleep(1)

        glutPostRedisplay()
        glFlush()

    def draw(self):
        self._carry_out_calculations()

        WIDTH, HEIGHT = self.width, self.height
        W_LEFT, W_RIGHT = (-WIDTH / 2), (
            WIDTH / 2
        )  # DISTANCE FROM EDGE TO CENTRE or vv
        W_BOTTOM, W_TOP = (-HEIGHT / 2), (
            HEIGHT / 2
        )  # DISTANCE FROM EDGE TO CENTRE or vv
        LEFT_RIGHT_BOTTOM_TOP = (
            W_LEFT,
            W_RIGHT,
            W_BOTTOM,
            W_TOP,
        )  # FOR CLIPPING WINDOW
        BLACK = (0.0, 0.0, 0.0, 0.7)

        glutInit()
        glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
        glutInitWindowSize(self.width, self.height)
        glutCreateWindow("Sutherland Hodgeman Polygon Clipping")
        glutDisplayFunc(self._draw_clipping)
        glClearColor(*BLACK)
        gluOrtho2D(*LEFT_RIGHT_BOTTOM_TOP)  # ORTHOGRAPHIC 2D SPACE
        glutMainLoop()


if __name__ == "__main__":
    clip = SutherlandHodgemanPolygonClipping(
        [150, 150, -150, -150],
        [(-200, 80), (50, 200), (120, 80), (100, -200), (-100, -100)],
    )
    clip.clip_polygon()
    clip.draw()
