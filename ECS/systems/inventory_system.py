"""Inventory System for managing inventories in the game.
"""
from ECS.components import Inventory
from ECS.component_handler import ComponentHandler

class InventorySystem:
    def __init__(self, ch: ComponentHandler) -> None:
        self.ch = ch

    def update(self) -> None:
        """Update the inventory system.
        """
        for entity_id in self.ch.get_entities_with_components([Inventory]):
            if entity_id is None:
                continue
            # inventory = self.ch.get_component(entity_id, Inventory)
            # Update inventory logic here
