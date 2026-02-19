import pyglet.gl as gl
import numpy as np
from meshes.base_mesh import BaseMesh

class QuadMesh(BaseMesh):
    def __init__(self, app):
        super().__init__()
        self.app = app

        # Set shader program from app
        self.program = self.app.shader_program#.water

        # Vertex format: 2 floats for texture coordinates, 3 floats for position
        self.vbo_format = "2f 3f"
        self.attrs = ('in_tex_coord', 'in_position')

        # Create VAO and VBO
        self.vao = self.get_vao()

    def get_vertex_data(self):
        # Vertex data: positions and texture coordinates
        vertices = np.array([
            (0, 0, 0), (1, 0, 1), (1, 0, 0),
            (0, 0, 0), (0, 0, 1), (1, 0, 1)
        ], dtype='float32')

        tex_coords = np.array([
            (0, 0), (1, 1), (1, 0),
            (0, 0), (0, 1), (1, 1)
        ], dtype='float32')

        # Combine texture coordinates and vertex positions into one array
        vertex_data = np.hstack([tex_coords, vertices])
        return vertex_data
