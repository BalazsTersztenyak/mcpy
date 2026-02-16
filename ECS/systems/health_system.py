"""Health System for managing entity health and handling death.
"""
from ECS.components import Health
from ECS.component_handler import ComponentHandler
from ECS.entity_handler import EntityHandler

class HealthSystem:
    """System responsible for managing entity health and handling death.
    """
    def __init__(self, ch: ComponentHandler, eh: EntityHandler) -> None:
        self.ch = ch
        self.eh = eh

    def update(self) -> None:
        """Update the health system, checking for entities with zero or negative 
        health and removing them.
        """
        for entity_id in self.ch.get_entities_with_components([Health]):
            if entity_id is None:
                continue
            health = self.ch.get_component(entity_id, Health)
            if health is None:
                continue
            if health.current <= 0:
                print(f"Entity {entity_id} has died.")
                self.eh.remove_entity(entity_id)
