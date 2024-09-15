import pyglet
import pyglet.gl as gl
import numpy as np
from settings import WIN_RES, WIN_POS

import terrain_gen

def main():
    window = MainWindow()
    pyglet.app.run()

class MainWindow(pyglet.window.Window):
    def __init__(self):
        super().__init__()

        self.clk = pyglet.clock.get_default()
        self.clk.tick()
        self.clk.schedule(self.fps)

        self.set_size(*WIN_RES)
        self.set_location(*WIN_POS)
        self.set_caption("main.py")

        # self.set_exclusive_mouse(True)
        
        gl.glClearColor(0.0, 0.0, 0.0, 1.0)

        self.terrain = terrain_gen.get_terrain(10, 10, 42)

    def on_draw(self):
        self.clear()
        self.draw_terrain()

    def draw_terrain(self):
        pass


        # gl.glBegin(gl.GL_QUADS)

        # for x in range(self.terrain.shape[0]):
        #     for y in range(self.terrain.shape[1]):
        #         gl.glColor3f(self.terrain[x][y], self.terrain[x][y], self.terrain[x][y])
        #         gl.glVertex2f(x, y)

        # gl.glEnd()

    def fps(self, dt):
        self.set_caption(f"FPS: {np.divide(1,dt):.0f}")
    
if __name__ == "__main__":
    main()