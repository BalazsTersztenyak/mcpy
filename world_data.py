# TODO : add world data
import math
from chunk_data import Chunk
class World:
    def __init__(self, app):
        self.app = app
        self.chunks = {}
        self.load()

    def load(self):
        for x in range(4):
            for y in range(4):
                self.chunks[(x, y)] = Chunk(x, y)

    def load_chunk(self, x, z):
        self.chunks[(x, z)] = Chunk(x, z)

    def unload_chunk(self, x, z):
        if (x, z) in self.chunks:
            self.chunks[(x, z)].unload()
            del self.chunks[(x, z)]
            self.chunks.remove((x, z))

    def get_block(self, xw, zw, y):
        xc, zc, x, z, y = self.convert_coord(xw, zw, y)
        chunk = self.get_chunk(xc, zc)
        return chunk.get_block(x, z, y)
    
    def set_block(self, xw, zw, y, block):
        xc, zc, x, z, y = self.convert_coord(xw, zw, y)
        chunk = self.get_chunk(xc, zc)
        chunk.set_block(x, z, y, block)

    def get_chunk(self, x, z):
        for chunk in self.chunks:
            if chunk.x == x and chunk.y == z:
                return chunk
        return None
    
    def update_top_block(self, xw, zw, y):
        xc, zc, x, z, y = self.convert_coord(xw, zw, y)
        chunk = self.get_chunk(xc, zc)
        chunk.update_top_block(x, z, y)

    def get_top_block(self, xw, zw):
        xc, zc, x, z, y = self.convert_coord(xw, zw, y)
        chunk = self.get_chunk(xc, zc)
        return chunk.get_top_block(x, z)
    
    def convert_coord(self, xw, zw, y):
        xc = math.floor(xw / Chunk.SIZE)
        zc = math.floor(zw // Chunk.SIZE)
        x = xw % Chunk.SIZE
        z = zw % Chunk.SIZE
        return xc, zc, x, z, y