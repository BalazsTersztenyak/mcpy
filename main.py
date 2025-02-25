import pyglet
import pyglet.gl as gl

from pyglet.math import Vec3

from settings import BG_COLOR
import window as win
from shader import get_program

def main():
    app = VoxelEngine()
    app.run()

class VoxelEngine:
    BG_COLOR = Vec3(0.58, 0.83, 0.99)

    def __init__(self):
        self.batch = pyglet.graphics.Batch()
        self.init_window()
        self.init_shaders()

    def init_window(self):
        self.window = win.Window(self)
        gl.glClearColor(*BG_COLOR, 1.0)

    def init_shaders(self):
        self.shader = get_program("basic")

    def update(self, dt):
        pass
        # self.window.set_caption(f"FPS: {1/dt:.2f}")
        
    def run(self):
        pyglet.clock.schedule_interval(self.update, 1/60)
        pyglet.app.run()

if __name__ == "__main__":
    main()