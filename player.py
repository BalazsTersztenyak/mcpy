from pyglet.window import key
from camera import Camera
import settings

class Player(Camera):
    def __init__(self, app, position=settings.PLAYER_POS, yaw=0, pitch=0):
        super().__init__(position, yaw, pitch)

        self.key_state = app.key_state
        self.mouse_state = app.mouse_state
        self.mouse_x, self.mouse_y = 0, 0

    def update(self, dt):
        self.keyboard_control(dt)
        self.mouse_control()
        super().update()

    def mouse_control(self, x, y, dx, dy):
        self.rotate_pitch(dy * settings.MOUSE_SENSITIVITY)
        self.rotate_yaw(dx * settings.MOUSE_SENSITIVITY)

    def keyboard_control(self, dt):
        vel = dt * settings.PLAYER_SPEED

        if self.key_state[key.W]:
            self.move_forward(vel)

        if self.key_state[key.S]:
            self.move_forward(vel)

        if self.key_state[key.A]:
            self.move_left(vel)

        if self.key_state[key.D]:
            self.move_right(vel)

        if self.key_state[key.SPACE]:
            self.move_up(vel)

        if self.key_state[key.LSHIFT]:
            self.move_down(vel)