# TODO : chunk class
from math import pi
import pickle

class Chunk:
    def __init__(self, x, z, size=16):
        self.x = x
        self.z = z
        self.SIZE = size
        self.blocks = {}
        self.load_chunk()
    
    def _load(self):
        for x in range(self.SIZE):
            for y in range(self.SIZE):
                for z in range(self.SIZE):
                    self.set_block(x, z, y, 1)  # Fill with stone (block ID 1)

    def load_chunk(self):
        try:
            self.blocks = pickle.load(open(f"save_files/chunk_{self.x}_{self.z}.dat", "rb"))
        except FileNotFoundError:
            self._load()

    def unload_chunk(self):
        pickle.dump((self.blocks), open(f"save_files/chunk_{self.x}_{self.z}.dat", "wb"))

    def get_block(self, x, z, y):
        return self.blocks.get((x, y, z), 0)
    
    def set_block(self, x, z, y, block):
        self.blocks[(x, y, z)] = block

    def update_block(self, x, z, y, block):
        raise NotImplementedError("Update block not implemented yet")
