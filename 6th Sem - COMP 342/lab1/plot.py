from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import random


width, height = 1024, 768
Points = []
Color = None
Coordinates_Color = None
lineRanges = None


def get_random_float():
    return random.randrange(50) / 50


def rcf():
    return get_random_float()


def clearScreen():
    """ """

    glClearColor(0.95, 0.95, 0.95, 0.3)
    gluOrtho2D(0, width, 0, height)


def plotPoints():
    """ """

    glClear(GL_COLOR_BUFFER_BIT)

    if Color.upper() == "RED":
        glColor3f(1.0, 0.0, 0.0)
    elif Color.upper() == "GREEN":
        glColor3f(0.0, 1.0, 0.0)
    elif Color.upper() == "BLUE":
        glColor3f(0.0, 0.0, 1.0)
    else:
        glColor3f(1.0, 1.0, 1.0)

    glPointSize(3.0)

    glBegin(GL_POINTS)
    for point in Points:
        glVertex2f(point[0], point[1])
    glEnd()

    glFlush()


def plotPointsMultipleColor():
    """ """

    glClear(GL_COLOR_BUFFER_BIT)

    for item in Coordinates:
        glColor3f(rcf(), rcf(), rcf())
        glPointSize(3.0)

        glBegin(GL_POINTS)
        for point in item:
            glVertex2f(point[0], point[1])
        glEnd()

    glFlush()


def plotInGlut(title: str, coordinates: list, color: str):
    """ """

    global Points, Color
    Points = coordinates
    Color = color

    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(title)
    glutDisplayFunc(plotPoints)
    clearScreen()
    glutMainLoop()


def plotMultipleInGlut(title: str, coordinates: list):
    global Coordinates
    Coordinates = coordinates

    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(500, 500)
    glutCreateWindow(title)
    glutDisplayFunc(plotPointsMultipleColor)
    clearScreen()
    glutMainLoop()
