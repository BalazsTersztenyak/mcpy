from ECS.components import Health
from ..component_handler import Component_Handler
from ..entity_handler import Entity_Handler

class HealthSystem:
    def __init__(self, cm: Component_Handler, eh: Entity_Handler) -> None:
        self.cm = cm
        self.eh = eh

    def update(self, dt: float) -> None:
        for entity_id in self.cm.get_entities_with_components([Health]):
            health = self.cm.get_component(entity_id, Health)
            if health.current <= 0:
                print(f"Entity {entity_id} has died.")
                self.eh.remove_entity(entity_id)