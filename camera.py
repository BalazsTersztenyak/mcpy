"""Camera class for handling view and projection matrices, as well as camera movement and rotation.
"""
import math
from pyglet.math import Vec3, Mat4, clamp

import settings

UP_WORLD = Vec3(0, 1, 0)

class Camera:
    """Camera class
    """
    def __init__(self, position, yaw, pitch):
        self.position = position
        self.yaw = math.radians(yaw)
        self.pitch = math.radians(pitch)
        self.camera_front = Vec3(0, 0, -1)
        self.right = Vec3(1, 0, 0)
        self.camera_up = Vec3(0, 1, 0)

        self.proj_mat = Mat4.perspective_projection(aspect=settings.ASPECT_RATIO,
                                                  z_near=settings.Z_NEAR,
                                                  z_far=settings.Z_FAR,
                                                  fov=settings.FOV_DEG)

        self.view_mat = Mat4()

        self.up = UP_WORLD

    #region Update
    def update(self, dt: float):
        """Update camera

        Args:
            dt (float): Time since last tick
        """
        self.update_vectors(dt)
        self.update_view_matrix()
        # print(self.position)

    def update_view_matrix(self):
        """Update the view matrix based on the current position and orientation of the camera.
        """
        self.view_mat = Mat4.look_at(self.position,
                                     self.position + self.camera_front,
                                     self.camera_up)

    def update_vectors(self, dt: float):
        """Update camera vectors based on current orientation and time delta.

        Args:
            dt (float): Time since last tick
        """
        dt *= settings.MOUSE_SENSITIVITY
        self.camera_front = Vec3(math.cos(self.yaw) * math.cos(self.pitch),
                          math.sin(self.pitch),
                          math.sin(self.yaw) * math.cos(self.pitch)).normalize()

        self.right = self.camera_front.cross(UP_WORLD).normalize()

        self.camera_up = self.right.cross(self.camera_front).normalize()
    #endregion

    #region Camera Controls
    def rotate_pitch(self, delta_y: float):
        """Update the camera's pitch based on the given delta_y, and clamp it to prevent flipping.

        Args:
            delta_y (float): The change in pitch, derived from mouse movement.
        """
        self.pitch -= delta_y
        self.pitch = clamp(self.pitch, -settings.PITCH_MAX, settings.PITCH_MAX)

    def rotate_yaw(self, delta_x: float):
        """Update the camera's yaw based on the given delta_x.

        Args:
            delta_x (float): The change in yaw, derived from mouse movement.
        """
        self.yaw += delta_x
    #endregion

    #region Movement
    def move_left(self, velocity):
        """Move the camera to the left.

        Args:
            velocity (float): The speed at which to move the camera.
        """
        self.position -= self.right * velocity

    def move_right(self, velocity):
        """Move the camera to the right.

        Args:
            velocity (float): The speed at which to move the camera.
        """
        self.position += self.right * velocity

    def move_up(self, velocity):
        """Move the camera up.

        Args:
            velocity (float): The speed at which to move the camera.
        """
        self.position += UP_WORLD * velocity

    def move_down(self, velocity):
        """Move the camera down.

        Args:
            velocity (float): The speed at which to move the camera.
        """
        self.position -= UP_WORLD * velocity

    def move_forward(self, velocity):
        """Move the camera forward.

        Args:
            velocity (float): The speed at which to move the camera.
        """
        self.position += self.camera_front * velocity

    def move_backward(self, velocity):
        """Move the camera backward.

        Args:
            velocity (float): The speed at which to move the camera.
        """
        self.position -= self.camera_front * velocity
    #endregion
