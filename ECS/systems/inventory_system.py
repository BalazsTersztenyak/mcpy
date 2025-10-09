from ECS.components import Inventory
from ..component_handler import Component_Handler

class InventorySystem:
    def __init__(self, cm: Component_Handler) -> None:
        self.cm = cm

    def update(self, dt: float) -> None:
        for entity_id in self.cm.get_entities_with_components([Inventory]):
            inventory = self.cm.get_component(entity_id, Inventory)
            # Update inventory logic here