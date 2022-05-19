from math import cos, radians, sin

from pyrr import Vector3, matrix44, vector, vector3


class Camera:
    def __init__(self):
        self.camera_pos = Vector3([0.0, 4.0, 3.0])
        self.camera_front = Vector3([0.0, 0.0, -1.0])
        self.camera_up = Vector3([0.0, 1.0, 0.0])
        self.camera_right = Vector3([1.0, 0.0, 0.0])

        self.mouse_click = False
        self.mouse_sensitivity = 0.25
        self.jaw = -90
        self.pitch = 0

    def get_view_matrix(self):
        """
        Get view matrix
        """
        # takes arguments 1st-eye position, 2nd- Target position, 3rd- Up direction
        return matrix44.create_look_at(
            self.camera_pos, self.camera_pos + self.camera_front, self.camera_up
        )

    def process_mouse_movement(self, x_offset, y_offset, constrain_pitch=True):
        """
        Process cursor mouse movements
        """

        x_offset *= self.mouse_sensitivity
        y_offset *= self.mouse_sensitivity

        self.jaw -= x_offset / 4  # convert x offset to jaw movement
        self.pitch -= y_offset / 4  # convert x offset to jaw movement

        if constrain_pitch:
            if self.pitch > 90:
                self.pitch = 90
            if self.pitch < -90:
                self.pitch = -90

        self.update_camera_vectors()

    # Camera method for the WASDQE movement
    def process_keyboard(self, direction, velocity):
        """
        Process keyboard key inputs into camera position vector
        i.e. location of the eye

        e.g., if FORWARD then camera front value increases with
        given velocity
        """

        if direction == "FORWARD":
            self.camera_pos += self.camera_front * velocity
        if direction == "BACKWARD":
            self.camera_pos -= self.camera_front * velocity
        if direction == "LEFT":
            self.camera_pos -= self.camera_right * velocity
        if direction == "RIGHT":
            self.camera_pos += self.camera_right * velocity
        if direction == "UP":
            self.camera_pos -= self.camera_up * velocity
        if direction == "DOWN":
            self.camera_pos += self.camera_up * velocity

    def update_camera_vectors(self):
        """
        Update camera/view vectors

        Processes any change in jaw, pitch values
        into vector coordinates for camera view
        """

        front = Vector3([0.0, 0.0, 0.0])
        front.x = cos(radians(self.jaw)) * cos(radians(self.pitch))
        front.y = sin(radians(self.pitch))
        front.z = sin(radians(self.jaw)) * cos(radians(self.pitch))

        self.camera_front = vector.normalise(front)
        self.camera_right = vector.normalise(
            vector3.cross(self.camera_front, Vector3([0.0, 1.0, 0.0]))
        )
        self.camera_up = vector.normalise(
            vector3.cross(self.camera_right, self.camera_front)
        )
