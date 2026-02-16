"""Handles input from the user, such as keyboard and mouse events.
"""
from pyglet.window.key import (MOD_SHIFT,
                                MOD_CTRL,
                                MOD_ALT,
                                MOD_WINDOWS,
                                MOD_COMMAND,
                                MOD_OPTION,
                                MOD_CAPSLOCK,
                                MOD_NUMLOCK,
                                MOD_SCROLLLOCK,
                                MOD_ACCEL)

class InputHandler:
    """A class to handle user input, such as keyboard and mouse events. It keeps 
    track of the state of keys and modifiers.
    """
    def __init__(self):
        self.modifiers = [MOD_SHIFT,
                        MOD_CTRL,
                        MOD_ALT,
                        MOD_WINDOWS,
                        MOD_COMMAND,
                        MOD_OPTION,
                        MOD_CAPSLOCK,
                        MOD_NUMLOCK,
                        MOD_SCROLLLOCK,
                        MOD_ACCEL]
        self.keys = {}
        print("InputHandler initialized with modifiers:", self.modifiers)


    def update_keys(self, symbol: int, modifiers: int, pressed = True):
        """Update the state of a key and modifier keys.

        Args:
            symbol (int): The key symbol that was pressed or released.
            modifiers (int): The active modifier keys.
            pressed (bool, optional): Whether the key was pressed or released. Defaults to True.
        """
        self.keys[symbol] = pressed
        for mod in self.modifiers:
            self.keys[mod] = bool(modifiers & mod)
        print(f"Key {symbol} was {'pressed' if pressed else 'released'}")

    def get_key_state(self, symbol: int) -> bool:
        """Get the current state of a key.

        Args:
            symbol (_type_): The key symbol to check.

        Returns:
            bool: True if the key is currently pressed, False otherwise.
        """
        return self.keys.get(symbol, False)
