from chunk_data import Chunk

def test_chunk_creation():
    chunk = Chunk(0, 0)
    assert type(chunk) is Chunk
    assert chunk.x == 0
    assert chunk.z == 0
    assert chunk.get_block(0, 0, 0) == 1  # Default block type is stone (1)
    chunk.unload_chunk()

def test_chunk_set_block():
    chunk = Chunk(0, 0)
    chunk.set_block(0, 0, 0, 2)  # Change to grass block
    assert chunk.get_block(0, 0, 0) == 2

def test_chunk_persistence():
    chunk = Chunk(0, 0)
    chunk.set_block(0, 0, 0, 2)  # Change to grass block
    chunk.unload_chunk()
    chunk2 = Chunk(0, 0)
    assert chunk2.get_block(0, 0, 0) == 2