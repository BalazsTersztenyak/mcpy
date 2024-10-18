import pyglet
import pyglet.gl as gl

from pyglet.math import Vec3, Mat4

from settings import WIN_RES, WIN_POS, BG_COLOR, ASPECT_RATIO, Z_NEAR, Z_FAR, FOV_DEG
from shader import get_program

from player import Player

def main():
    app = VoxelEngine()
    app.run()

class VoxelEngine:
    def __init__(self):
        self.window = pyglet.window.Window(width=WIN_RES[0], height=WIN_RES[1], 
                                           caption="Voxel Engine", resizable=True)
        
        self.window.set_location(WIN_POS[0], WIN_POS[1])

        self.dispatcher = pyglet.event.EventDispatcher()

        gl.glClearColor(*BG_COLOR, 1.0)

        self.shader = get_program("basic")

        self.window.set_exclusive_mouse(True)

        self.key_state = pyglet.window.key.KeyStateHandler()
        self.window.push_handlers(self.key_state)
        self.mouse_state = pyglet.window.mouse.MouseStateHandler()
        self.window.push_handlers(self.mouse_state)

        self.player = Player(self)
        # self.dispatcher.push_handlers(self.player.mouse_control)

        self.view_mat = self.player.view_mat
        self.proj_mat = self.player.proj_mat
        
        self.shader['vp'] = self.proj_mat @ self.view_mat

        self.shader['model'] = Mat4()

        self.vertices  = [
            -0.5, -0.5, -3.0,
            -0.5, 0.5, -3.0,
            0.5, 0.5, -3.0,
            0.5, -0.5, -3.0
        ]

        self.indices = [
            0, 1, 2, 2, 3, 0
        ]

        self.colors = [
            1.0, 0.0, 0.0, 1.0,
            0.0, 1.0, 0.0, 1.0,
            0.0, 0.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0
        ]

        self.batch = pyglet.graphics.Batch()

        self.vertex_list = self.shader.vertex_list_indexed(len(self.vertices) // 3, 
                                                            gl.GL_TRIANGLES, 
                                                            batch=self.batch, 
                                                            indices=self.indices,
                                                            vertices=('f', self.vertices),
                                                            colors=('f', self.colors))
        

    def update(self, dt):
        self.window.clear()
        self.window.set_caption(f"FPS: {1/dt:.2f}")
        self.player.update(dt)
        self.shader['vp'] = self.proj_mat @ self.player.view_mat
        self.batch.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        self.player.mouse_control(dx, dy)

    def run(self):
        pyglet.clock.schedule_interval(self.update, 1/60)
        pyglet.app.run()

if __name__ == "__main__":
    main()