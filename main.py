"""This is the main file for the project. 
It initializes the window, shaders, and runs the main loop."""
import pyglet
# import pyglet.gl as gl

from pyglet.math import Vec3

# from settings import BG_COLOR
import window as win
from shader import get_program

def main() -> None:
    """Initializes the app
    """
    app = VoxelEngine()
    app.run()

class VoxelEngine:
    """Initialize game engine
    """
    BG_COLOR = Vec3(0.58, 0.83, 0.99)

    def __init__(self) -> None:
        self.batch = pyglet.graphics.Batch()
        self.init_window()
        self.init_shaders()

    def init_window(self) -> None:
        """Initialize window
        """
        self.window = win.Window(self)
        self.window.set_clear_color(*self.BG_COLOR, 1.0)

    def init_shaders(self) -> None:
        """Initialize shaders
        """
        self.shader = get_program("basic")

    def update(self, dt: float) -> None:
        """Main game loop

        Args:
            dt (float): Time since last tick
        """
        # self.window.update(dt) # Update the window, if needed

    def run(self) -> None:
        """Schedule the main loop at 60 FPS and run the app
        """
        pyglet.clock.schedule_interval(self.update, 1/60)
        pyglet.app.run()

if __name__ == "__main__":
    main()
