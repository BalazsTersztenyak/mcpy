import pyglet
import pyglet.gl as gl

class Window(pyglet.window.Window):
    def __init__(self, app):
        super().__init__(resizable=True)

        self.set_size(800, 600)
        self.set_caption("Test window")

        self.set_location(100, 100)

        self.fps_display = pyglet.window.FPSDisplay(self)

        self.app = app

    def on_draw(self) -> None:
        self.clear()    # window.clear()
        self.app.batch.draw()   # window.batch.draw()
        self.fps_display.draw()

    def on_resize(self, width, height):
        gl.glViewport(0, 0, width, height)