from dataclasses import dataclass

@dataclass
class Position:
    x: float
    y: float
    z: float

@dataclass
class Velocity:
    dx: float
    dy: float
    dz: float

@dataclass
class Acceleration:
    ddx: float
    ddy: float
    ddz: float

@dataclass
class Health:
    current: int
    maximum: int

@dataclass
class Inventory:
    items: list[tuple[str, int, int]]  # item name, quantity, slot
    capacity: int # number of slots
    input_sides: list[bool] # sides for input ([top, bottom, left, right, front, back])
    output_sides: list[bool] # sides for output ([top, bottom, left, right, front, back])