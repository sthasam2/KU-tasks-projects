import glfw
import pyrr
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader

from camera import Camera
from obj_loader import ObjLoader
from texture_loader import load_texture

#########################
# GLOBAL VARIABLES
#########################

WIDTH, HEIGHT = 1280, 720
cam = Camera()
lastX, lastY = WIDTH / 2, HEIGHT / 2
first_mouse = True
left_mb_click = False
left, right, forward, backward, up, down = False, False, False, False, False, False


#########################
# CALLBACK FUNCTIONS
#########################


def key_input_clb(window, key, scancode, action, mode):
    """Keyboard input callback"""

    global left, right, forward, backward, up, down

    # EXIT
    if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
        glfw.set_window_should_close(window, True)

    # FORWARD
    if key == glfw.KEY_W and action == glfw.PRESS:
        forward = True
    elif key == glfw.KEY_W and action == glfw.RELEASE:
        forward = False

    # BACKWARD
    if key == glfw.KEY_S and action == glfw.PRESS:
        backward = True
    elif key == glfw.KEY_S and action == glfw.RELEASE:
        backward = False

    # LEFT
    if key == glfw.KEY_A and action == glfw.PRESS:
        left = True
    elif key == glfw.KEY_A and action == glfw.RELEASE:
        left = False

    # RIGHT
    if key == glfw.KEY_D and action == glfw.PRESS:
        right = True
    elif key == glfw.KEY_D and action == glfw.RELEASE:
        right = False

    # UP
    if key == glfw.KEY_Q and action == glfw.PRESS:
        up = True
    elif key == glfw.KEY_Q and action == glfw.RELEASE:
        up = False

    # DOWN
    if key == glfw.KEY_E and action == glfw.PRESS:
        down = True
    elif key == glfw.KEY_E and action == glfw.RELEASE:
        down = False


def do_movement():
    """
    Do the movement, call this function in the main loop

    Pans the camera as the value for left, right, forward, backward changes
    """

    if left:
        cam.process_keyboard("LEFT", 0.1)
    if right:
        cam.process_keyboard("RIGHT", 0.1)
    if forward:
        cam.process_keyboard("FORWARD", 0.1)
    if backward:
        cam.process_keyboard("BACKWARD", 0.1)
    if up:
        cam.process_keyboard("UP", 0.1)
    if down:
        cam.process_keyboard("DOWN", 0.1)


def mouse_click_clb(window, button, action, mods):
    """
    Mouse Input callback

    Handles Mouse click events in the window (Only LMB)
    """
    global left_mb_click

    if button == glfw.MOUSE_BUTTON_LEFT:
        if action == glfw.PRESS:
            left_mb_click = True

        elif action == glfw.RELEASE:
            left_mb_click = False


def mouse_scroll_clb(window, x_offset, y_offset):
    """
    Mouse Scroll callback

    Handles Mouse scroll events in the window
    """
    global forward, backward

    # FORWARD
    if y_offset > 0:
        cam.process_keyboard("FORWARD", 1)

    # BACKWARD
    if y_offset < 0:
        cam.process_keyboard("BACKWARD", 1)

    # print(x_offset, y_offset)


def mouse_look_clb(window, x_pos, y_pos):
    """
    Mouse position callback function

    Handles data of mouse position in the window
    """

    global first_mouse, lastX, lastY

    if first_mouse:
        lastX = x_pos
        lastY = y_pos
        first_mouse = False

    x_offset = x_pos - lastX
    y_offset = lastY - y_pos

    lastX = x_pos
    lastY = y_pos

    # print(lastX, lastY)

    if left_mb_click:
        cam.process_mouse_movement(x_offset, y_offset)


def window_resize_clb(window, width, height):
    """
    Window resize callback function

    Adjusts window view based on window size
    """

    glViewport(0, 0, width, height)
    projection = pyrr.matrix44.create_perspective_projection_matrix(
        45, width / height, 0.1, 100
    )
    glUniformMatrix4fv(proj_loc, 1, GL_FALSE, projection)


################################################################
# C-CODE FOR SHADERS
#
# learn more at https://learnopengl.com/Getting-started/Shaders
################################################################

## Vertex shader
# https://www.khronos.org/opengl/wiki/Vertex_Shader

vertex_src = """
# version 330

layout(location = 0) in vec3 a_position;
layout(location = 1) in vec2 a_texture;
layout(location = 2) in vec3 a_normal;

uniform mat4 model;
uniform mat4 projection;
uniform mat4 view;

out vec2 v_texture;

void main()
{
    gl_Position = projection * view * model * vec4(a_position, 1.0);
    v_texture = a_texture;
}
"""

## FRAGMENT SHADER
# https://www.khronos.org/opengl/wiki/Fragment_Shader

fragment_src = """
# version 330

in vec2 v_texture;

out vec4 out_color;

uniform sampler2D s_texture;

void main()
{
    out_color = texture(s_texture, v_texture);
}
"""

#########################
#  INITIALIZE WINDOW
#########################

# initializing glfw library
if not glfw.init():
    raise Exception("glfw can not be initialized!")

# creating the window
window = glfw.create_window(WIDTH, HEIGHT, "My OpenGL window", None, None)

# check if window was created
if not window:
    glfw.terminate()
    raise Exception("glfw window can not be created!")

# set window's position
glfw.set_window_pos(window, 400, 200)


############################
# WINDOW RELATED CALLBACKS
############################

# set the callback function for window resize
glfw.set_window_size_callback(window, window_resize_clb)

# set the mouse click callback
glfw.set_mouse_button_callback(window, mouse_click_clb)

# set the mouse scroll callback
glfw.set_scroll_callback(window, mouse_scroll_clb)

# set the mouse position callback
glfw.set_cursor_pos_callback(window, mouse_look_clb)

# set the keyboard input callback
glfw.set_key_callback(window, key_input_clb)

# make the context current
glfw.make_context_current(window)


#########################
#  LOAD OBJECTS
#########################

#
## load here the 3d meshes
dice_indices, dice_buffer = ObjLoader.load_model("meshes/dice.obj")
board_indices, board_buffer = ObjLoader.load_model("meshes/ludo.obj")

#
## CREATE SHADERS
shader = compileProgram(
    compileShader(vertex_src, GL_VERTEX_SHADER),
    compileShader(fragment_src, GL_FRAGMENT_SHADER),
)

#
##  Initialize VAO and VBO for objects
VAO = glGenVertexArrays(2)
VBO = glGenBuffers(2)

########
# DICE
########

# dice VAO
glBindVertexArray(VAO[0])
# dice Vertex Buffer Object
glBindBuffer(GL_ARRAY_BUFFER, VBO[0])
glBufferData(GL_ARRAY_BUFFER, dice_buffer.nbytes, dice_buffer, GL_STATIC_DRAW)
# dice vertices
glEnableVertexAttribArray(0)
glVertexAttribPointer(
    0, 3, GL_FLOAT, GL_FALSE, dice_buffer.itemsize * 8, ctypes.c_void_p(0)
)
# dice textures
glEnableVertexAttribArray(1)
glVertexAttribPointer(
    1, 2, GL_FLOAT, GL_FALSE, dice_buffer.itemsize * 8, ctypes.c_void_p(12)
)
# dice normals
glVertexAttribPointer(
    2, 3, GL_FLOAT, GL_FALSE, dice_buffer.itemsize * 8, ctypes.c_void_p(20)
)
glEnableVertexAttribArray(2)


#########
# BOARD
#########

# board VAO
glBindVertexArray(VAO[1])
# board Vertex Buffer Object
glBindBuffer(GL_ARRAY_BUFFER, VBO[1])
glBufferData(GL_ARRAY_BUFFER, board_buffer.nbytes, board_buffer, GL_STATIC_DRAW)

# board vertices
glEnableVertexAttribArray(0)
glVertexAttribPointer(
    0, 3, GL_FLOAT, GL_FALSE, board_buffer.itemsize * 8, ctypes.c_void_p(0)
)
# board textures
glEnableVertexAttribArray(1)
glVertexAttribPointer(
    1, 2, GL_FLOAT, GL_FALSE, board_buffer.itemsize * 8, ctypes.c_void_p(12)
)
# board normals
glVertexAttribPointer(
    2, 3, GL_FLOAT, GL_FALSE, board_buffer.itemsize * 8, ctypes.c_void_p(20)
)
glEnableVertexAttribArray(2)


#########################
# LOAD OBJECT TEXTURES
#########################

textures = glGenTextures(2)
load_texture("meshes/dice.jpg", textures[0])
load_texture("meshes/ludo.jpg", textures[1])


#############################
# OPENGL DISPLAY PROPERTIES
#############################

glUseProgram(shader)  # use shaders
glClearColor(0, 0.1, 0.1, 1)  # black screen
glEnable(GL_DEPTH_TEST)  # enable depth
glEnable(GL_BLEND)  # enabling blend/ transparency
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)  # transparency functions


##############################
#  VIEW AND OBJECT MATRICES
##############################

# projection matrix i.e. perspective projection
projection = pyrr.matrix44.create_perspective_projection_matrix(
    45, WIDTH / HEIGHT, 0.1, 100
)
# position of dice with respect ot view space vector
dice_pos = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, 5, 0]))
# position of board with respect ot view space vector
board_pos = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, 0, 0]))

#
# getUniformLocation
# returns an integer that represents the location of a specific uniform variable within a program object.

# getting memory location from shader
model_loc = glGetUniformLocation(shader, "model")
proj_loc = glGetUniformLocation(shader, "projection")
view_loc = glGetUniformLocation(shader, "view")

glUniformMatrix4fv(proj_loc, 1, GL_FALSE, projection)


#########################
#  DRIVER CODE
#########################

# the main application loop
while not glfw.window_should_close(window):

    # Check for events like mouse click or key presses
    glfw.poll_events()
    do_movement()  # perform movement after event

    # refreshing buffer
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # get camera view coordinates
    view = cam.get_view_matrix()
    # set shader's view location to obtained view coordinates
    glUniformMatrix4fv(view_loc, 1, GL_FALSE, view)

    # get rotation matrices
    rot_y = pyrr.Matrix44.from_y_rotation(0.8 * glfw.get_time())
    rot_x = pyrr.Matrix44.from_x_rotation(0.8 * glfw.get_time())

    # apply rotations to dice
    model = pyrr.matrix44.multiply(rot_y, dice_pos)
    model = pyrr.matrix44.multiply(rot_x, model)

    # draw the dice
    glBindVertexArray(VAO[0])
    glBindTexture(GL_TEXTURE_2D, textures[0])
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, model)
    glDrawArrays(GL_TRIANGLES, 0, len(dice_indices))

    # draw the board
    glBindVertexArray(VAO[1])
    glBindTexture(GL_TEXTURE_2D, textures[1])
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, board_pos)
    glDrawArrays(GL_TRIANGLES, 0, len(board_indices))

    # replace previous window context with new context
    # essentially refreshing screen
    glfw.swap_buffers(window)

# terminate glfw, free up allocated resources
glfw.terminate()
