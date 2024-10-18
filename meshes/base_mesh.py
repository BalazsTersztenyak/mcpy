import numpy as np
from pyglet import gl

class BaseMesh:
    def __init__(self):
        # OpenGL context is handled by pyglet window
        self.program = None
        self.vbo_format = None
        self.attrs = None
        self.vao = None
        self.vbo = None

    def get_vertex_data(self) -> np.array:
        """This method should return the vertex data"""
        raise NotImplementedError

    def get_vao(self):
        # Get the vertex data
        vertex_data = self.get_vertex_data()
        vertex_data = (gl.GLfloat * len(vertex_data))(*vertex_data)

        # Generate Vertex Buffer Object (VBO)
        self.vbo = gl.GLuint()
        gl.glGenBuffers(1, gl.byref(self.vbo))
        gl.glBindBuffer(gl.GL_ARRAY_BUFFER, self.vbo)
        gl.glBufferData(gl.GL_ARRAY_BUFFER, len(vertex_data) * 4, vertex_data, gl.GL_STATIC_DRAW)

        # Generate Vertex Array Object (VAO)
        self.vao = gl.GLuint()
        gl.glGenVertexArrays(1, gl.byref(self.vao))
        gl.glBindVertexArray(self.vao)

        # Enable vertex attributes and set pointers based on format and attributes
        stride = 0
        if self.vbo_format:
            stride = sum(int(f[:-1]) * 4 for f in self.vbo_format.split())
        offset = 0

        for i, attr in enumerate(self.attrs):
            location = gl.glGetAttribLocation(self.program, attr.encode('utf-8'))
            if location != -1:
                gl.glEnableVertexAttribArray(location)
                gl.glVertexAttribPointer(location, int(self.vbo_format.split()[i][:-1]), gl.GL_FLOAT, gl.GL_FALSE, stride, gl.ctypes.c_void_p(offset))
                offset += int(self.vbo_format.split()[i][:-1]) * 4

        gl.glBindVertexArray(0)
        gl.glBindBuffer(gl.GL_ARRAY_BUFFER, 0)

    def render(self):
        if self.vao is None:
            raise ValueError("VAO is not initialized. Call get_vao first.")
        
        gl.glUseProgram(self.program)
        gl.glBindVertexArray(self.vao)
        gl.glDrawArrays(gl.GL_TRIANGLES, 0, len(self.get_vertex_data()) // len(self.vbo_format.split()))
        gl.glBindVertexArray(0)
        gl.glUseProgram(0)
