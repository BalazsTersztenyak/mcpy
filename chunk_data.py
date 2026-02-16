"""This module defines the Chunk class, which represents a section of the game world. 
"""
# from math import pi
import pickle

class Chunk:
    """Class to handle chunk data
    """
    def __init__(self, x, z, size=16):
        self.x = x
        self.z = z
        self.SIZE = size
        self.blocks = {}
        self.load_chunk()

    def _check_in_chunk(self, x, z, y):
        return 0 <= x < self.SIZE and 0 <= z < self.SIZE and 0 <= y < self.SIZE

    def load_chunk(self):
        """Loads chunk data from file
        """
        try:
            self.blocks = pickle.load(open(f"save_files/chunk_{self.x}_{self.z}.dat", "rb"))
        except FileNotFoundError:
            self.blocks = {}

    def unload_chunk(self):
        """Saves chunk data to file
        """
        pickle.dump((self.blocks), open(f"save_files/chunk_{self.x}_{self.z}.dat", "wb"))

    def get_block(self, x: int, z: int, y: int):
        """Return block at coordinate (x, y, z)

        Args:
            x (int): x coordinate of block in chunk
            z (int): z coordinate of block in chunk
            y (int): y coordinate of block in chunk

        Raises:
            ValueError: _description_

        Returns:
            _type_: _description_
        """
        if not self._check_in_chunk(x, z, y):
            raise ValueError("Block coordinates out of bounds")

        return self.blocks.get((x, y, z), 0)

    def set_block(self, x: int, z: int, y: int, block: int):
        """Sets a block at the given coordinates in the chunk.

        Args:
            x (int): x coordinate of block in chunk
            z (int): z coordinate of block in chunk
            y (int): y coordinate of block in chunk
            block (int): The block type to set at the given coordinates
        """
        if not self._check_in_chunk(x, z, y):
            raise ValueError("Block coordinates out of bounds")
        self.blocks[(x, y, z)] = block
