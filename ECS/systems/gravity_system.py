"""Gravity System
"""
from ECS.components import Velocity
from ECS.component_handler import ComponentHandler

class GravitySystem:
    """A system that applies gravity to entities with a Velocity component.
    """
    def __init__(self, ch: ComponentHandler) -> None:
        self.ch = ch
        self.gravity = [0, -9.81, 0]  # Gravity acceleration in m/s^2

    def update(self, dt: float) -> None:
        """Update the velocities of entities affected by gravity.

        Args:
            dt (float): Time since last tick.
        """
        for entity_id in self.ch.get_entities_with_components([Velocity]):
            if entity_id is None:
                continue
            vel = self.ch.get_component(entity_id, Velocity)
            if vel is None:
                continue
            vel.vx += self.gravity[0] * dt
            vel.vy += self.gravity[1] * dt
            vel.vz += self.gravity[2] * dt
