from ECS.components import Position, Velocity
from ..component_handler import Component_Manager

class MovementSystem:
    def __init__(self, cm: Component_Manager):
        self.cm = cm

    def update(self, dt: float) -> None:

        for entity_id in self.cm.get_entities_with_components([Position, Velocity]):
            pos = self.cm.get_component(entity_id, Position)
            vel = self.cm.get_component(entity_id, Velocity)
            pos.x += vel.vx * dt
            pos.y += vel.vy * dt
            pos.z += vel.vz * dt
