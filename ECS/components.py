"""ECS Components
"""
from dataclasses import dataclass

@dataclass
class Position:
    """A component representing the position of an entity in 3D space.
    """
    x: float
    y: float
    z: float

@dataclass
class Velocity:
    """A component representing the velocity of an entity in 3D space.
    """
    dx: float
    dy: float
    dz: float

@dataclass
class Acceleration:
    """A component representing the acceleration of an entity in 3D space.
    """
    ddx: float
    ddy: float
    ddz: float

@dataclass
class Health:
    """A component representing the health of an entity.
    """
    current: int
    maximum: int

@dataclass
class Inventory:
    """A component representing the inventory of an entity.
    """
    items: list[tuple[str, int, int]]  # item name, quantity, slot
    capacity: int # number of slots
    input_sides: list[bool] # sides for input ([top, bottom, left, right, front, back])
    output_sides: list[bool] # sides for output ([top, bottom, left, right, front, back])
