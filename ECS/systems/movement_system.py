"""Movement System for updating entity positions based on their velocities.
"""
from ECS.components import Acceleration, Position, Velocity
from ECS.component_handler import ComponentHandler

class MovementSystem:
    """System that updates the position of entities based on their velocity.
    """
    def __init__(self, ch: ComponentHandler):
        self.ch = ch

    def update(self, dt: float) -> None:
        """Update the position of entities based on their velocity.

        Args:
            dt (float): Time since last tick
        """
        for entity_id in self.ch.get_entities_with_components([Position, Velocity]):
            if entity_id is None:
                continue
            pos = self.ch.get_component(entity_id, Position)
            vel = self.ch.get_component(entity_id, Velocity)
            acc = self.ch.get_component(entity_id, Acceleration)
            if pos is None or vel is None:
                continue
            pos.x += vel.vx * dt
            pos.y += vel.vy * dt
            pos.z += vel.vz * dt

            if vel is None or acc is None:
                continue
            vel.vx += acc.ax * dt
            vel.vy += acc.ay * dt
            vel.vz += acc.az * dt
