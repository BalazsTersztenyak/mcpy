import pyglet
# import pyglet.gl as gl

from pyglet.math import Vec3

# from settings import BG_COLOR
import window as win
from shader import get_program

def main() -> None:
    app = VoxelEngine()
    app.run()

class VoxelEngine:
    BG_COLOR = Vec3(0.58, 0.83, 0.99)

    def __init__(self) -> None:
        self.batch = pyglet.graphics.Batch()
        self.init_window()
        self.init_shaders()

    def init_window(self) -> None:
        self.window = win.Window(self)
        self.window.set_clear_color(*self.BG_COLOR, 1.0)

    def init_shaders(self) -> None:
        self.shader = get_program("basic")

    def update(self, dt: float) -> None:
        pass
        # self.window.update(dt) # Update the window, if needed

    def run(self) -> None:
        pyglet.clock.schedule_interval(self.update, 1/60)
        pyglet.app.run()

if __name__ == "__main__":
    main()