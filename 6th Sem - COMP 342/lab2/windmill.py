from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from transformation import Transformation
from midpoint_ellipse import midpoint_ellipse


class Windmill:
    width, height = 1900, 1000
    support = [[-60, -400], [60, -400], [30, -40], [0, 0], [-30, -40]]
    blade = [[-300, 0], [0, 0], [-50, 20], [-50, 40]]
    hub = midpoint_ellipse([0, 0], [10, 10])
    speed = 0.005

    def __init__(self, win_resolution=(width, height)) -> None:
        self.width, self.height = win_resolution

    def _process_signal(self, key, *_):
        if key == b"0":
            self.speed = 0.005
        elif key == b"=":
            self.speed += 0.01
        elif key == b"-":
            self.speed -= 0.01

    def _draw_polygon(self, vertices):
        glPointSize(5.0)
        glBegin(GL_POLYGON)
        for (x, y) in vertices:
            glVertex2f(x, y)
        glEnd()

    def _draw_windmill(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        glColor4f(0.3, 0.2, 0.1, 1.0)
        self._draw_polygon(self.support)

        glColor4f(0.80, 0.50, 0.0, 0.9)
        for _ in range(3):
            self.blade = Transformation(self.blade).rotation2D(120)
            self._draw_polygon(self.blade)

        glColor4f(0.8, 0.8, 0.0, 1.0)
        self._draw_polygon(self.hub)

        self.blade = Transformation(self.blade).rotation2D(self.speed)
        glutPostRedisplay()
        glFlush()

    def draw(self):
        WIDTH, HEIGHT = self.width, self.height
        LEFT, RIGHT = (-WIDTH / 2), (WIDTH / 2)  # DISTANCE FROM EDGE TO CENTRE or vv
        BOTTOM, TOP = (-HEIGHT / 2), (HEIGHT / 2)  # DISTANCE FROM EDGE TO CENTRE or vv
        LEFT_RIGHT_BOTTOM_TOP = (LEFT, RIGHT, BOTTOM, TOP)  # FOR CLIPPING WINDOW
        BLACK = (0.0, 0.0, 0.0, 0.7)

        glutInit()
        glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
        glutInitWindowSize(self.width, self.height)
        glutCreateWindow("Windmill")
        glutDisplayFunc(self._draw_windmill)
        glutKeyboardFunc(self._process_signal)
        glClearColor(*BLACK)
        gluOrtho2D(*LEFT_RIGHT_BOTTOM_TOP)  # ORTHOGRAPHIC 2D SPACE
        glutMainLoop()


if __name__ == "__main__":
    windmill = Windmill()
    windmill.draw()
    print("done")
