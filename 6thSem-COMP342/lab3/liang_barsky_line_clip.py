from time import sleep

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


class LiangBarskyLineClipping:
    """ """

    # Defining XW_MAX, YW_MAX and XW_MIN, YW_MIN for viewport rectangle
    XW_MAX = None
    YW_MAX = None
    XW_MIN = None
    YW_MIN = None

    # Original Line ends
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

    def __init__(
        self,
        window_region: list,
        line_start: list = None,
        line_end: list = None,
    ) -> None:
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

    def _window_vetices(self):
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

    def _original_line_ends(self):
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
            self.clipped_line_ends = self.liang_barsky_clip()
        return self.clipped_line_ends

    def _carry_out_calculations(self):
        self._original_line_ends()
        self._clipped_line_ends()

    # Implementing Liang-Barsky algorithm
    # Clipping a line from P1 = (x1, y1) to P2 = (x2, y2)
    def liang_barsky_clip(self):
        dx = self.x2 - self.x1
        dy = self.y2 - self.y1
        pks = [-dx, dx, -dy, dy]
        qks = [
            self.x1 - self.XW_MIN,
            self.XW_MAX - self.x1,
            self.y1 - self.YW_MIN,
            self.YW_MAX - self.y1,
        ]
        u1, u2 = 0, 1

        for (pk, qk) in zip(pks, qks):
            # For all the boundaries
            if pk == 0 and qk < 0:  # if line is parallel to any axes and lies outside
                return
            if pk == 0:  # catch and skip division by zero
                continue
            u = qk / pk
            if pk < 0:
                u1 = max(u1, u)
            else:
                u2 = min(u2, u)

        if u1 <= u2:  # line is not completely outside
            x1, y1 = self.x1, self.y1
            clipped_x1 = x1 + u1 * dx
            clipped_x2 = x1 + u2 * dx
            clipped_y1 = y1 + u1 * dy
            clipped_y2 = y1 + u2 * dy

            print(
                "Line accepted from %.2f, %.2f to %.2f, %.2f"
                % (clipped_x1, clipped_y1, clipped_x2, clipped_y2)
            )
            return [clipped_x1, clipped_y1], [clipped_x2, clipped_y2]

        # line completely outside
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
        glutCreateWindow("Liang Barsky Line Clipping")
        glutDisplayFunc(self._draw_clipping)
        glClearColor(*BLACK)
        gluOrtho2D(*LEFT_RIGHT_BOTTOM_TOP)  # ORTHOGRAPHIC 2D SPACE
        glutMainLoop()


if __name__ == "__main__":
    clip = LiangBarskyLineClipping([200, 200, -200, -200], [302, 252], [-350, -250])
    clip.liang_barsky_clip()
    clip.draw()

    # clip = LiangBarskyLineClipping([200, 200, -200, -200], [-202, -202], [-550, 250])
    # clip.liang_barsky_clip()
    # clip.draw()
