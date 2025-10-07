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

