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

    def get_vao(self):
        # Get vertex data
        vertex_data = self.get_vertex_data()
        vertex_data = (gl.GLfloat * len(vertex_data))(*vertex_data)

        # Generate VBO (vertex buffer)
        self.vbo = gl.GLuint()
        gl.glGenBuffers(1, gl.byref(self.vbo))
        gl.glBindBuffer(gl.GL_ARRAY_BUFFER, self.vbo)
        gl.glBufferData(gl.GL_ARRAY_BUFFER, len(vertex_data) * 4, vertex_data, gl.GL_STATIC_DRAW)

        # Generate VAO (vertex array object)
        self.vao = gl.GLuint()
        gl.glGenVertexArrays(1, gl.byref(self.vao))
        gl.glBindVertexArray(self.vao)

        # Enable vertex attributes based on format (2f for texture, 3f for position)
        stride = 5 * 4  # 2 floats for tex_coords + 3 floats for position = 5 floats per vertex
        offset = 0

        # Set up attribute pointers
        for i, attr in enumerate(self.attrs):
            location = gl.glGetAttribLocation(self.program, attr.encode('utf-8'))
            if location != -1:
                gl.glEnableVertexAttribArray(location)
                if i == 0:  # Texture coordinates (2 floats)
                    gl.glVertexAttribPointer(location, 2, gl.GL_FLOAT, gl.GL_FALSE, stride, gl.ctypes.c_void_p(offset))
                    offset += 2 * 4  # 2 floats * 4 bytes
                elif i == 1:  # Position (3 floats)
                    gl.glVertexAttribPointer(location, 3, gl.GL_FLOAT, gl.GL_FALSE, stride, gl.ctypes.c_void_p(offset))
                    offset += 3 * 4  # 3 floats * 4 bytes

        # Unbind VAO and VBO
        gl.glBindVertexArray(0)
        gl.glBindBuffer(gl.GL_ARRAY_BUFFER, 0)

    def render(self):
        if self.vao is None:
            raise ValueError("VAO is not initialized. Call get_vao first.")

        # Use shader program and bind VAO
        gl.glUseProgram(self.program)
        gl.glBindVertexArray(self.vao)

        # Draw the quad using 6 vertices (2 triangles)
        gl.glDrawArrays(gl.GL_TRIANGLES, 0, 6)

        # Unbind VAO and program after drawing
        gl.glBindVertexArray(0)
        gl.glUseProgram(0)
