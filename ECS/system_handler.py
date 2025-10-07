from .systems import *

class System_Handler:
    def __init__(self):
        self.systems = []

    def update(self, dt):
        for system in self.systems:
            system.update(dt)