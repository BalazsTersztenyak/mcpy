"""Component Handler
"""
from collections import defaultdict
from typing import Generator

class ComponentHandler:
    """A simple component manager for an Entity-Component-System (ECS) architecture.
    """
    def __init__(self) -> None:
        self._components = defaultdict(dict)

    def add_component(self, entity_id: str, component: type) -> None:
        """Adds a component to an entity.

        Args:
            entity_id (str): The unique identifier of the entity.
            component (type): The component instance to be added to the entity.
        """
        self._components[component][entity_id] = component

    def remove_component(self, entity_id: str, component_type: type) -> None:
        """Removes a component from an entity.

        Args:
            entity_id (str): The unique identifier of the entity.
            component_type (type): The type of component to be removed.
        """
        if entity_id in self._components[component_type]:
            del self._components[component_type][entity_id]

    def get_component(self, entity_id: str, component_type: type) -> type | None:
        """Returns a component of a specific type for an entity.

        Args:
            entity_id (str): The unique identifier of the entity.
            component_type (type): The type of component to retrieve.


        Returns:
            type | None: The component instance if it exists, otherwise None.
        """
        return self._components[component_type].get(entity_id)

    def get_entities_with_components(self, *component_types: list[type]) -> Generator[None | str]:
        """Returns a generator of entity IDs that have all the specified component types.

        Yields:
            Generator[None | str]: The entity IDs that have all the specified component types.
        """
        if not component_types:
            return
        sets = [set(self._components[ctype].keys()) for ctype in component_types]
        for entity in set.intersection(*sets):
            yield entity
