from collections import defaultdict
from typing import Generator

class Component_Handler:
    def __init__(self) -> None:
        self._components = defaultdict(dict)

    def add_component(self, entity_id: str, component: type) -> None:
        self._components[component][entity_id] = component

    def remove_component(self, entity_id: str, component_type: type) -> None:
        if entity_id in self._components[component_type]:
            del self._components[component_type][entity_id]

    def get_component(self, entity_id: str, component_type: type) -> type | None:
        return self._components[component_type].get(entity_id)

    def get_entities_with_components(self, *component_types: type) -> Generator[None | str]:
        if not component_types:
            return
        sets = [set(self._components[ctype].keys()) for ctype in component_types]
        for entity in set.intersection(*sets):
            yield entity