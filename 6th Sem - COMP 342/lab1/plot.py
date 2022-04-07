from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import random


WIDTH, HEIGHT = 1900, 1000
LEFT, RIGHT = (-WIDTH / 2), (WIDTH / 2)  # DISTANCE FROM EDGE TO CENTRE or vv
BOTTOM, TOP = (-HEIGHT / 2), (HEIGHT / 2)  # DISTANCE FROM EDGE TO CENTRE or vv
LEFT_RIGHT_BOTTOM_TOP = (LEFT, RIGHT, BOTTOM, TOP)  # FOR CLIPPING WINDOW
# LEFT_RIGHT_BOTTOM_TOP = (0, RIGHT, 0, TOP)  # FOR CLIPPING WINDOW

WHITE = (0.95, 0.95, 0.95, 0.7)
BLACK = (0.0, 0.0, 0.0, 0.7)
YELLOW = (1.0, 1.0, 0.5, 0.5)
RED = (1.0, 0.0, 0.0, 1.0)
GREEN = (0.0, 1.0, 0.0, 1.0)
BLUE = (0.0, 0.0, 0.0, 1.0)


Points = []
Color = None
Coordinates_Color = None
lineRanges = None
EnableAxes = 1


def _get_random_float():
    return random.randrange(50) / 50


def random_color():
    return (_get_random_float(), _get_random_float(), _get_random_float(), 0.5)


########################
# GLUT CUSTOMIZATION
########################


def initScreen():
    """Initialize Screen"""

    glClearColor(*BLACK)
    gluOrtho2D(*LEFT_RIGHT_BOTTOM_TOP)  # ORTHOGRAPHIC 2D SPACE
    enableColorTransparency()


def enableColorTransparency():
    """Enabling Transparency i.e. Alpha"""

    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)


def enableLinePattern():
    """Enabling stipple i.e. line patterns"""

    glEnable(GL_LINE_STIPPLE)
    glLineStipple(3, 0x6666)  # dotted line pattern


########################
# PLOTTING OBJECTS
########################


def plotAxes():
    """ """

    enableColorTransparency()  # Enabling Transparency i.e. Alpha
    enableLinePattern()  # Enabling stipple i.e. line patterns

    # setting color and pixel size
    glColor4f(*YELLOW)
    glLineWidth(3.0)

    # x axis
    glBegin(GL_LINES)
    glVertex2f(LEFT + 15, 0.0)
    glVertex2f(RIGHT - 15, 0.0)
    # y axis
    glVertex2f(0.0, TOP - 15)
    glVertex2f(0.0, BOTTOM + 15)
    glEnd()

    glBegin(GL_TRIANGLES)
    # x axis arrows
    glVertex2f(LEFT, 0.0)
    glVertex2f(LEFT + 15, 15.0)
    glVertex2f(LEFT + 15, -15.0)
    glVertex2f(RIGHT, 0.0)
    glVertex2f(RIGHT - 15, 15.0)
    glVertex2f(RIGHT - 15, -15.0)
    # Y axis arrows
    glVertex2f(0.0, BOTTOM)
    glVertex2f(15.0, BOTTOM + 15)
    glVertex2f(-15.0, BOTTOM + 15)
    glVertex2f(0.0, TOP)
    glVertex2f(15.0, TOP - 15)
    glVertex2f(-15.0, TOP - 15)
    glEnd()

    glFlush()


def plotPoints():
    """ """

    glClear(GL_COLOR_BUFFER_BIT)

    plotAxes()

    if Color.upper() == "RED":
        glColor4f(*RED)
    elif Color.upper() == "GREEN":
        glColor4f(*GREEN)
    elif Color.upper(*BLUE) == "BLUE":
        glColor4f()
    else:
        glColor4f(*WHITE)

    glPointSize(3.0)

    glBegin(GL_POINTS)
    for point in Points:
        glVertex2f(point[0], point[1])
    glEnd()

    glFlush()


def plotPointsMultipleColor():
    """ """

    glClear(GL_COLOR_BUFFER_BIT)

    if EnableAxes != 0:
        plotAxes()

    for item in Coordinates:
        glColor4f(*random_color())
        glPointSize(3.0)

        glBegin(GL_POINTS)
        for point in item:
            glVertex2f(point[0], point[1])
        glEnd()

    glFlush()


########################
# INITIALIZING GLUT
########################


def startGlutPlot(title: str, coordinates: list, color: str):
    """ """

    global Points, Color
    Points = coordinates
    Color = color

    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(WIDTH, HEIGHT)
    glutInitWindowPosition(50, 50)
    glutCreateWindow(title)
    glutDisplayFunc(plotPoints)
    initScreen()
    glutMainLoop()


def startGlutMultipleItemPlot(title: str, coordinates: list):
    global Coordinates
    Coordinates = coordinates

    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
    glutInitWindowSize(WIDTH, HEIGHT)
    glutInitWindowPosition(500, 500)
    glutCreateWindow(title)
    glutDisplayFunc(plotPointsMultipleColor)
    initScreen()
    glutMainLoop()


def startPiePlot(title: str, coordinates: list):
    global Coordinates, EnableAxes
    Coordinates = coordinates
    EnableAxes = 0

    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
    glutInitWindowSize(WIDTH, HEIGHT)
    glutInitWindowPosition(500, 500)
    glutCreateWindow(title)
    glutDisplayFunc(plotPointsMultipleColor)
    initScreen()
    glutMainLoop()


if __name__ == "__main__":
    startGlutPlot("Demo", [[1, 1]], "blue")
