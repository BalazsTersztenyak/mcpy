# TODO : chunk class
from json import load
from math import pi
import pickle

class Chunk:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.SIZE = 16
        self.blocks = []
        self.entities = []
        self.top_block = [0 for _ in range(self.SIZE * self.SIZE)]
        self.load()
    
    def load(self):
        for _ in range(self.SIZE * self.SIZE * self.SIZE):
            self.blocks.append(0)

    def load_chunk(self):
        try:
            self.blocks, self.entities, self.top_block = pickle.load(open(f"chunk_{self.x}_{self.y}.dat", "rb"))
        except FileNotFoundError:
            self.load()

    def unload_chunk(self):
        pickle.dump((self.blocks, self.entities, self.top_block), open(f"chunk_{self.x}_{self.y}.dat", "wb"))

    def get_block(self, x, z, y):
        return self.blocks[self._get_index(x, y, z)]
    
    def set_block(self, x, z, y, block):
        self.blocks[self._get_index(x, y, z)] = block

    def update_top_block(self, x, z, y):
        if y >= self.get_top_block(x, z):
            self._set_top_block(x, z, y)

    def get_top_block(self, x, z):
        return self.top_block[self._get_index(x, z)]
    
    def _set_top_block(self, x, z, block):
        self.top_block[self._get_index(x, z)] = block

    def _get_index(self, x, y, z):
        return x + (z * self.SIZE) + (y * self.SIZE * self.SIZE)
    
    def _get_index(self, x, z):
        return x + (z * self.SIZE)