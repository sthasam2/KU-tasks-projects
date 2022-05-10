"""Python program to implement Cohen Sutherland algorithm for line clipping."""

from time import sleep

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


class CohenSutherlandLineClipping:
    """ """

    # Region codes
    INSIDE = 0  # 0000
    LEFT = 1  # 0001
    RIGHT = 2  # 0010
    BOTTOM = 4  # 0100
    TOP = 8  # 1000

    # Defining XW_MAX, YW_MAX and XW_MIN, YW_MIN for viewport rectangle
    XW_MAX = None
    YW_MAX = None
    XW_MIN = None
    YW_MIN = None

    # Line ends
    x1 = None
    y1 = None
    x2 = None
    y2 = None

    original_line_ends = None
    clipped_line_ends = None

    # display display_step i.e.
    # 0: original line -> 1: window for clipping -> 2: clipped with window -> 3: clipped
    display_step = 0

    width, height = 1900, 1000
    window_color = (0.4, 0.4, 0.0, 0.5)
    original_line_color = (0.90, 0.20, 0.0, 0.9)
    clipped_line_color = (0.20, 0.90, 0.0, 0.9)

    def __init__(self, window_region: list, line_start: list, line_end: list) -> None:
        """
        window_region: <list>[XW_MAX, YW_MAX, XW_MIN, YW_MIN]
        line_start: <list>[x1, y1]
        line_end: <list>[x2, y2]
        """
        assert (
            len(window_region) == 4
        ), "Window region must include [XW_MAX, YW_MAX, XW_MIN, YW_MIN]"
        assert len(line_start) == 2, "Line start must have [x,y]"
        assert len(line_end) == 2, "Line end must have [x,y]"

        self.XW_MAX, self.YW_MAX, self.XW_MIN, self.YW_MIN = window_region
        self.x1, self.y1 = line_start
        self.x2, self.y2 = line_end

    def _window_vetices(self) -> tuple:
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

    def _original_line_ends(self) -> list:
        """Returns tuple: <Start>[x,y], <End>[x,y]"""

        if self.original_line_ends == None:
            self.original_line_ends = (
                [self.x1, self.y1],
                [self.x2, self.y2],
            )
        return self.original_line_ends

    def _clipped_line_ends(self):
        """Returns tuple: <Clipped Start>[x,y], <Clipped End>[x,y]"""

        if self.clipped_line_ends == None:
            self.clipped_line_ends = self.cohen_sutherland_clip()
        return self.clipped_line_ends

    def _carry_out_calculations(self):
        self._original_line_ends()
        self._clipped_line_ends()

    # Function to compute region code for a point(x, y)
    def _computeCode(self, x, y):
        code = self.INSIDE
        if x < self.XW_MIN:  # to the left of rectangle
            code |= self.LEFT
        elif x > self.XW_MAX:  # to the right of rectangle
            code |= self.RIGHT
        if y < self.YW_MIN:  # below the rectangle
            code |= self.BOTTOM
        elif y > self.YW_MAX:  # above the rectangle
            code |= self.TOP

        return code

    # Implementing Cohen-Sutherland algorithm
    # Clipping a line from P1 = (x1, y1) to P2 = (x2, y2)
    def cohen_sutherland_clip(self):

        XW_MAX, YW_MAX, XW_MIN, YW_MIN = (
            self.XW_MAX,
            self.YW_MAX,
            self.XW_MIN,
            self.YW_MIN,
        )
        x1, y1, x2, y2 = self.x1, self.y1, self.x2, self.y2

        # Compute region codes for P1, P2
        code1 = self._computeCode(x1, y1)
        code2 = self._computeCode(x2, y2)
        accept = False

        while True:
            # If both endpoints lie within rectangle
            if code1 == 0 and code2 == 0:
                accept = True
                break

            # If both endpoints are outside rectangle
            elif (code1 & code2) != 0:
                break

            # Some segment lies within the rectangle
            else:
                # Line Needs clipping
                # At least one of the points is outside,
                # select it
                x = 1.0
                y = 1.0
                if code1 != 0:
                    code_out = code1
                else:
                    code_out = code2

                # Find intersection point
                # using formulas y = y1 + slope * (x - x1),
                # x = x1 + (1 / slope) * (y - y1)
                if code_out & self.TOP:
                    # point is above the clip rectangle
                    x = x1 + (x2 - x1) * (YW_MAX - y1) / (y2 - y1)
                    y = YW_MAX

                elif code_out & self.BOTTOM:
                    # point is below the clip rectangle
                    x = x1 + (x2 - x1) * (YW_MIN - y1) / (y2 - y1)
                    y = YW_MIN

                elif code_out & self.RIGHT:
                    # point is to the right of the clip rectangle
                    y = y1 + (y2 - y1) * (XW_MAX - x1) / (x2 - x1)
                    x = XW_MAX

                elif code_out & self.LEFT:
                    # point is to the left of the clip rectangle
                    y = y1 + (y2 - y1) * (XW_MIN - x1) / (x2 - x1)
                    x = XW_MIN

                # Now intersection point x, y is found
                # We replace point outside clipping rectangle
                # by intersection point
                if code_out == code1:
                    x1 = x
                    y1 = y
                    code1 = self._computeCode(x1, y1)

                else:
                    x2 = x
                    y2 = y
                    code2 = self._computeCode(x2, y2)

        if accept:
            print("Line accepted from %.2f, %.2f to %.2f, %.2f" % (x1, y1, x2, y2))
            return [x1, y1], [x2, y2]
        else:
            print("Line rejected")
            return None

    def _draw_line(self, vertices):
        if vertices is not None:
            glPointSize(5.0)
            glBegin(GL_LINES)
            for (x, y) in vertices:
                glVertex2f(x, y)
            glEnd()

    def _draw_polygon(self):
        vertices = self._window_vetices()
        glPointSize(5.0)
        glBegin(GL_POLYGON)
        for (x, y) in vertices:
            glVertex2f(x, y)
        glEnd()

    def _draw_clipping(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        if self.display_step == 0:
            glColor4f(*self.original_line_color)
            self._draw_line(self.original_line_ends)
            self.display_step = 1

        elif self.display_step == 1:
            glColor4f(*self.window_color)
            self._draw_polygon()
            glColor4f(*self.original_line_color)
            self._draw_line(self.original_line_ends)
            self.display_step = 2

        elif self.display_step == 2:
            glColor4f(*self.window_color)
            self._draw_polygon()
            glColor4f(*self.clipped_line_color)
            self._draw_line(self.clipped_line_ends)
            self.display_step = 3

        elif self.display_step == 3:
            glColor4f(*self.clipped_line_color)
            self._draw_line(self.clipped_line_ends)
            self.display_step = 0

        sleep(1)

        glutPostRedisplay()
        glFlush()

    def draw(self):
        self._carry_out_calculations()

        WIDTH, HEIGHT = self.width, self.height
        LEFT, RIGHT = (-WIDTH / 2), (WIDTH / 2)  # DISTANCE FROM EDGE TO CENTRE or vv
        BOTTOM, TOP = (-HEIGHT / 2), (HEIGHT / 2)  # DISTANCE FROM EDGE TO CENTRE or vv
        LEFT_RIGHT_BOTTOM_TOP = (LEFT, RIGHT, BOTTOM, TOP)  # FOR CLIPPING WINDOW
        BLACK = (0.0, 0.0, 0.0, 0.7)

        glutInit()
        glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
        glutInitWindowSize(self.width, self.height)
        glutCreateWindow("Cohen Sutherland Line Clipping")
        glutDisplayFunc(self._draw_clipping)
        glClearColor(*BLACK)
        gluOrtho2D(*LEFT_RIGHT_BOTTOM_TOP)  # ORTHOGRAPHIC 2D SPACE
        glutMainLoop()


if __name__ == "__main__":
    clip = CohenSutherlandLineClipping([200, 100, -200, -100], [-202, -152], [250, 150])
    clip.cohen_sutherland_clip()
    clip.draw()

    clip = CohenSutherlandLineClipping(
        [200, 100, -200, -100], [-202, -202], [550, -250]
    )
    clip.cohen_sutherland_clip()
    clip.draw()
