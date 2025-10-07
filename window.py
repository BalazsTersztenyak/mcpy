import pyglet
import pyglet.gl as gl
import main
from input_handling import Input_handler

class Window(pyglet.window.Window):
    def __init__(self, app: main.VoxelEngine) -> None:
        """Initializes the window and sets up the shader."""
        super().__init__(resizable=True)

        self.set_size(800, 600)
        self.set_caption("Test window")

        self.set_location(100, 100)

        self.fps_display = pyglet.window.FPSDisplay(self)

        self.app = app

        self.input_handler = Input_handler()

    def on_draw(self) -> None:
        self.clear()    # window.clear()
        self.app.batch.draw()   # window.batch.draw()
        self.fps_display.draw()

    def on_resize(self, width: int, height: int) -> None:
        gl.glViewport(0, 0, width, height)

    def set_clear_color(self, r: float, g: float, b: float, a: float = 1.0) -> None:
        gl.glClearColor(r, g, b, a)

    def on_key_press(self, symbol, modifiers):
        self.input_handler.update_keys(symbol, modifiers, True)

    def on_key_release(self, symbol, modifiers):
        self.input_handler.update_keys(symbol, modifiers, False)