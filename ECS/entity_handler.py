from uuid import uuid4

class Entity_Handler:
    def __init__(self) -> None:
        self._entities: set = set()

    def create_entity(self) -> str:
        entity_id: str = str(uuid4())
        self._entities.add(entity_id)
        return entity_id

    def add_entity(self, entity_id: str)-> None:
        self._entities.add(entity_id)

    def remove_entity(self, entity_id: str) -> None:
        self._entities.discard(entity_id)