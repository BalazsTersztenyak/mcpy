"""Window management and rendering using pyglet.
"""
import pyglet
import pyglet.gl as gl
import main
from input_handling import InputHandler

#pylint: disable=abstract-method
class Window(pyglet.window.Window):
    """A class representing the application window, 
    responsible for rendering and handling user input.
    """
    def __init__(self, app: main.VoxelEngine) -> None:
        """Initializes the window and sets up the shader."""
        super().__init__(resizable=True)

        self.set_size(800, 600)
        self.set_caption("Test window")

        self.set_location(100, 100)

        self.fps_display = pyglet.window.FPSDisplay(self)

        self.app = app

        self.input_handler = InputHandler()

    def on_draw(self) -> None:
        self.clear()    # window.clear()
        self.app.batch.draw()   # window.batch.draw()
        self.fps_display.draw()

    def on_resize(self, width: int, height: int) -> None:
        gl.glViewport(0, 0, width, height)

    def set_clear_color(self, r: float, g: float, b: float, a: float = 1.0) -> None:
        """Sets color to fill the window with on clear.

        Args:
            r (float): red value
            g (float): green value
            b (float): blue value
            a (float, optional): alpha value. Defaults to 1.0.
        """
        gl.glClearColor(r, g, b, a)

    def on_key_press(self, symbol, modifiers):
        self.input_handler.update_keys(symbol, modifiers, True)

    def on_key_release(self, symbol, modifiers):
        self.input_handler.update_keys(symbol, modifiers, False)
