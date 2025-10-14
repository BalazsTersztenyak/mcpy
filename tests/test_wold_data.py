from world_data import World
from chunk_data import Chunk

def test_world_initialization():
    app = None  # Mock or dummy app object
    world: World = World(app)
    assert world.app == app
    assert isinstance(world.chunks, dict)

def test_load_chunk():
    app = None
    world: World = World(app)
    world.load_chunk(0, 0)
    assert (0, 0) in world.chunks
    assert isinstance(world.chunks[(0, 0)], Chunk)
    assert world.chunks[(0, 0)].x == 0
    assert world.chunks[(0, 0)].z == 0

def test_unload_chunk():
    app = None
    world: World = World(app)
    world.load_chunk(0, 0)
    world.unload_chunk(0, 0)
    assert (0, 0) not in world.chunks

def test_get_set_block():
    app = None
    world: World = World(app)
    world.load_chunk(0, 0)
    
    # Set a block and then get it
    world.set_block(1, 1, 1, 5)  # Set block ID 5 at (1, 1, 1)
    block_id: int = world.get_block(1, 1, 1)
    assert block_id == 5

    # Test getting a block that hasn't been set (should return 0)
    block_id = world.get_block(2, 2, 2)
    assert block_id == 0