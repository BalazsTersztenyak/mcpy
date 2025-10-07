from pyglet.window.key import *

class Input_handler():

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


    def update_keys(self, symbol, modifiers, pressed = True):
        self.keys[symbol] = pressed
        #for mod in self.modifiers:
        #    self.keys[mod]
        print(f"Key {symbol} was {'pressed' if pressed else 'released'}")

    def get_key_state(self, symbol):
        return self.keys.get(symbol, False)