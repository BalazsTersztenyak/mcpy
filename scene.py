from settings import *
import pyglet
from pyglet.gl import *
# from world import World
# from world_objects.voxel_marker import VoxelMarker
# from world_objects.water import Water
# from world_objects.clouds import Clouds
from meshes.quad_mesh import QuadMesh

class Scene:
    def __init__(self, app):
        self.app = app
        # self.world = World(self.app)
        # self.voxel_marker = VoxelMarker(self.world.voxel_handler)
        # self.water = Water(app)
        # self.clouds = Clouds(app)
        self.quad = QuadMesh(app)

    def update(self):
        # Update the world, voxel marker, and clouds
        # self.world.update()
        # self.voxel_marker.update()
        # self.clouds.update()
        pass

    def render(self):
        # Render the world (chunks)
        # self.world.render()

        # Disable face culling
        # glDisable(GL_CULL_FACE)
        # self.clouds.render()
        # self.water.render()

        # # Enable face culling back
        # glEnable(GL_CULL_FACE)

        # # Render voxel marker (for selection)
        # self.voxel_marker.render()

        self.quad.render()
