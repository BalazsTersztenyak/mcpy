"""EntityHandler is responsible for managing entities in the ECS framework. 
It provides methods to create, add, and remove entities. Each entity is represented
by a unique identifier (UUID). The EntityHandler maintains a set of active entities,
allowing for efficient management and retrieval of entities within the system.
"""
from uuid import uuid4

class EntityHandler:
    """The EntityHandler class manages entities in an Entity-Component-System (ECS) framework.
    """
    def __init__(self) -> None:
        self._entities: set = set()

    def create_entity(self) -> str:
        """Creates a new entity with a unique identifier and adds it to the set of active entities.

        Returns:
            str: The unique identifier of the newly created entity.
        """
        entity_id: str = str(uuid4())
        self._entities.add(entity_id)
        return entity_id

    def add_entity(self, entity_id: str)-> None:
        """Adds an existing entity to the set of active entities.

        Args:
            entity_id (str): The unique identifier of the entity to be added.
        """
        self._entities.add(entity_id)

    def remove_entity(self, entity_id: str) -> None:
        """Removes an entity from the set of active entities.

        Args:
            entity_id (str): The unique identifier of the entity to be removed.
        """
        self._entities.discard(entity_id)
