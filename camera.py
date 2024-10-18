from pyglet.math import Vec3, Mat4, clamp
import math

import settings

class Camera:
    def __init__(self, position, yaw, pitch):
        self.position = position
        self.yaw = math.radians(yaw)
        self.pitch = math.radians(pitch)

        self.proj_mat = Mat4.perspective_projection(aspect=settings.ASPECT_RATIO, 
                                                  z_near=settings.Z_NEAR, 
                                                  z_far=settings.Z_FAR,
                                                  fov=settings.FOV_DEG)
        
        self.view_mat = Mat4()

        self.up = Vec3(0, 1, 0)

    def update(self):
        self.update_vectors()
        self.update_view_matrix()

    def update_view_matrix(self):
        self.view_mat = Mat4.look_at(self.position, self.position + self.front, self.up)

    def update_vectors(self):
        self.front = Vec3(math.cos(self.yaw) * math.cos(self.pitch), 
                          math.sin(self.pitch),
                          math.sin(self.yaw) * math.cos(self.pitch)).normalize()
        
        self.right = self.front.cross(Vec3(0, 1, 0)).normalize()

        self.up = self.right.cross(self.front).normalize()
        
    def rotate_pitch(self, delta_y):
        self.pitch -= delta_y
        self.pitch = clamp(self.pitch, -settings.PITCH_MAX, settings.PITCH_MAX)

    def rotate_yaw(self, delta_x):
        self.yaw += delta_x

    def move_left(self, velocity):
        self.position -= self.right * velocity

    def move_right(self, velocity):
        self.position += self.right * velocity

    def move_up(self, velocity):
        self.position += Vec3(0, 1, 0) * velocity

    def move_down(self, velocity):
        self.position -= Vec3(0, 1, 0) * velocity

    def move_forward(self, velocity):
        self.position += self.front * velocity

    def move_backward(self, velocity):
        self.position -= self.front * velocity