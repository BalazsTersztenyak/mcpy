from pyglet.math import Vec3, Mat4, clamp
import math

import settings

<<<<<<< HEAD
WORLD_UP = Vec3(0, 1, 0)
=======
UP_WORLD = Vec3(0, 1, 0)
>>>>>>> a70a58ee209dc469e95ef72718df9d64bbd8c8ba

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

<<<<<<< HEAD
        self.camera_up = Vec3(0, 1, 0)
=======
        self.up = UP_WORLD
>>>>>>> a70a58ee209dc469e95ef72718df9d64bbd8c8ba

    #region Update
    def update(self):
        self.update_vectors()
        self.update_view_matrix()
        # print(self.position)

    def update_view_matrix(self):
        self.view_mat = Mat4.look_at(self.position, self.position + self.camera_front, self.camera_up)

    def update_vectors(self):
        self.camera_front = Vec3(math.cos(self.yaw) * math.cos(self.pitch), 
                          math.sin(self.pitch),
                          math.sin(self.yaw) * math.cos(self.pitch)).normalize()
        
<<<<<<< HEAD
        self.right = self.camera_front.cross(WORLD_UP).normalize()
=======
        self.right = self.front.cross(UP_WORLD).normalize()
>>>>>>> a70a58ee209dc469e95ef72718df9d64bbd8c8ba

        self.camera_up = self.right.cross(self.camera_front).normalize()
    #endregion

    #region Camera Controls
    def rotate_pitch(self, delta_y):
        self.pitch -= delta_y
        self.pitch = clamp(self.pitch, -settings.PITCH_MAX, settings.PITCH_MAX)

    def rotate_yaw(self, delta_x):
        self.yaw += delta_x
    #endregion

    #region Movement
    def move_left(self, velocity):
        self.position -= self.right * velocity

    def move_right(self, velocity):
        self.position += self.right * velocity

    def move_up(self, velocity):
<<<<<<< HEAD
        self.position += WORLD_UP * velocity

    def move_down(self, velocity):
        self.position -= WORLD_UP * velocity
=======
        self.position += UP_WORLD * velocity

    def move_down(self, velocity):
        self.position -= UP_WORLD * velocity
>>>>>>> a70a58ee209dc469e95ef72718df9d64bbd8c8ba

    def move_forward(self, velocity):
        self.position += self.camera_front * velocity

    def move_backward(self, velocity):
        self.position -= self.camera_front * velocity
    #endregion