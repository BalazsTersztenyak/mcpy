"""Module to handle world data, including loading and unloading chunks, 
and getting/setting blocks in the world.
"""
import math
from typing import TYPE_CHECKING
from chunk_data import Chunk

if TYPE_CHECKING:
    from main import VoxelEngine

class World:
    """Class to handle chunk data
    """
    def __init__(self, app: "VoxelEngine") -> None:
        self.app: "VoxelEngine" = app
        self.chunks: dict[tuple[int, int], Chunk] = {}
        self._load()

    def _load(self) -> None:
        for x in range(4):
            for y in range(4):
                self.chunks[(x, y)] = Chunk(x, y)

    def load_chunk(self, x: int, z: int) -> None:
        """Load chunk to memory at coordinate (x, z)

        Args:
            x (int): coodrinate of chunk
            z (int): coordinate of chunk
        """
        self.chunks[(x, z)] = Chunk(x, z)

    def unload_chunk(self, x: int, z: int) -> None:
        """Unload chunk from memory at coordinate (x, z)

        Args:
            x (int): coodrinate of chunk
            z (int): coordinate of chunk
        """
        if (x, z) in self.chunks:
            self.chunks[(x, z)].unload_chunk()
            self.chunks.pop((x, z), None)

    def get_block(self, xw: int, zw: int, y: int) -> int:
        """Returns block at coordinate (x, y, z) in world coodinates

        Args:
            xw (int): world coordinate
            zw (int): world coordinate
            y (int): world coordinate

        Returns:
            int: Block id
        """
        xc, zc, x, z, y = self._convert_coord(xw, zw, y)
        chunk = self.get_chunk(xc, zc)
        if chunk:
            return chunk.get_block(x, z, y)
        return 0

    def set_block(self, xw: int, zw: int, y: int, block: int) -> None:
        """Sets block at coordinate (x, y, z) in world coodinates

        Args:
            xw (int): world coordinate
            zw (int): world coordinate
            y (int): world coordinate
            block (int): Block id to set
        """
        coords: tuple[int, int, int, int, int] = self._convert_coord(xw, zw, y)
        chunk: Chunk | None = self.get_chunk(coords[0], coords[1])

        if chunk:
            chunk.set_block(coords[2], coords[3], coords[4], block)
        else:
            raise ValueError(f'Chunk at ({coords[0]}, {coords[1]}) not loaded.')

    def get_chunk(self, x: int, z: int) -> Chunk | None:
        """Gets the chunk at coordinate (x, z)

        Args:
            x (int): coordinate of chunk
            z (int): coordinate of chunk

        Returns:
            Chunk | None: Chunk data or None if the chunk data doesn't exist
        """
        for chunk in self.chunks.values():
            if chunk.x == x and chunk.z == z:
                return chunk
        return None

    def _convert_coord(self, xw: int, zw: int, y: int) -> tuple[int, int, int, int, int]:
        xc: int = math.floor(xw / 16)
        zc: int = math.floor(zw / 16)
        x: int = xw % 16
        z: int = zw % 16
        return xc, zc, x, z, y
