"""SystemHandler manages all the systems in the ECS architecture
"""
from .systems.gravity_system import GravitySystem
from .systems.movement_system import MovementSystem
from .systems.health_system import HealthSystem
from .systems.inventory_system import InventorySystem
from .component_handler import ComponentHandler
from .entity_handler import EntityHandler

class SystemHandler:
    """SystemHandler manages all the systems in the ECS architecture. It holds 
    references to the ComponentHandler and EntityHandler, and updates all systems each frame.
    """
    def __init__(self, ch: ComponentHandler, eh: EntityHandler):
        self.systems = [
            GravitySystem(ch),
            MovementSystem(ch),
            HealthSystem(ch, eh),
            InventorySystem(ch)
        ]
        self.ch = ch
        self.eh = eh

    def update(self, dt: float) -> None:
        """Update all systems in the system handler.

        Args:
            dt (float): Time since last tick.
        """
        for system in self.systems:
            system.update(dt)
