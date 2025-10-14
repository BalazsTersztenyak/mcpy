import os
from chunk_data import Chunk

def test_chunk_creation():
    x: int = 0
    z: int = 0
    if os.path.exists(f"save_files/chunk_{x}_{z}.dat"):
        os.remove(f"save_files/chunk_{x}_{z}.dat")
    chunk = Chunk(x, z)
    assert type(chunk) is Chunk
    assert chunk.x == x
    assert chunk.z == z
    assert chunk.get_block(0, 0, 0) == 0  # Default block type is air (0)

def test_chunk_set_block():
    x: int = 0
    z: int = 0
    chunk = Chunk(x, z)
    chunk.set_block(0, 0, 0, 2)  # Change to grass block
    assert chunk.get_block(0, 0, 0) == 2

def test_chunk_persistence():
    x: int = 0
    z: int = 0
    if os.path.exists(f"save_files/chunk_{x}_{z}.dat"):
        os.remove(f"save_files/chunk_{x}_{z}.dat")
    chunk = Chunk(x, z)
    chunk.set_block(0, 0, 0, 2)  # Change to grass block
    chunk.unload_chunk()
    chunk2 = Chunk(x, z)  # Reload chunk
    assert chunk2.get_block(0, 0, 0) == 2