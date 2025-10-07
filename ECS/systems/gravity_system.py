from ECS.components import Velocity
from ..component_handler import Component_Manager

class MovementSystem:
    def __init__(self, cm: Component_Manager):
        self.cm = cm
        self.gravity = [0, -9.81, 0]  # Gravity acceleration in m/s^2

    def update(self, dt: float) -> None:

        for entity_id in self.cm.get_entities_with_components([Velocity]):
            vel = self.cm.get_component(entity_id, Velocity)
            vel.vx += self.gravity[0] * dt
            vel.vy += self.gravity[1] * dt
            vel.vz += self.gravity[2] * dt
