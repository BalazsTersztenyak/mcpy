import glfw
from OpenGL.GL import *
import numpy as np

# Vertex shader source code
vertex_shader_src = """
    #version 330 core

    layout (location = 0) in vec3 aPos;
    layout (location = 1) in vec2 aTexCoord;

    out vec2 TexCoord;

    uniform mat4 model;
    uniform mat4 view;
    uniform mat4 projection;

    void main()
    {
        gl_Position = projection * view * model * vec4(aPos, 1.0);
        TexCoord = aTexCoord;
    }
"""

# Fragment shader source code
fragment_shader_src = """
    #version 330 core

    out vec4 FragColor;

    in vec2 TexCoord;

    uniform sampler2D texture1;

    void main()
    {
        FragColor = texture(texture1, TexCoord);
    }
"""

# Function to compile shaders
def compile_shader(shader_source, shader_type):
    shader = glCreateShader(shader_type)
    glShaderSource(shader, shader_source)
    glCompileShader(shader)

    # Check for compilation errors
    if not glGetShaderiv(shader, GL_COMPILE_STATUS):
        error = glGetShaderInfoLog(shader).decode()
        raise RuntimeError(f"Shader compilation error: {error}")

    return shader

def main():
    # Initialize the library
    if not glfw.init():
        return
    
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(640, 480, "Hello World", None, None)
    if not window:
        glfw.terminate()
        return

    # Make the window's context current
    glfw.make_context_current(window)

    # Compile shaders
    # vertex_shader = compile_shader(vertex_shader_src, GL_VERTEX_SHADER)
    # fragment_shader = compile_shader(fragment_shader_src, GL_FRAGMENT_SHADER)

    # Create shader program
    # shader_program = glCreateProgram()
    # glAttachShader(shader_program, vertex_shader)
    # glAttachShader(shader_program, fragment_shader)
    # glLinkProgram(shader_program)

    # Check for linking errors
    # if not glGetProgramiv(shader_program, GL_LINK_STATUS):
    #     error = glGetProgramInfoLog(shader_program).decode()
    #     raise RuntimeError(f"Shader linking error: {error}")

    # Delete shaders
    # glDeleteShader(vertex_shader)
    # glDeleteShader(fragment_shader)

    # Define vertices, texture coordinates, and indices for a single cube
    vertices = np.array([
        # Front face
        -0.5, -0.5,  0.5,  0.0, 0.0,
        0.5, -0.5,  0.5,  1.0, 0.0,
        0.5,  0.5,  0.5,  1.0, 1.0,
        -0.5,  0.5,  0.5,  0.0, 1.0,

        # Back face
        -0.5, -0.5, -0.5,  1.0, 0.0,
        0.5, -0.5, -0.5,  0.0, 0.0,
        0.5,  0.5, -0.5,  0.0, 1.0,
        -0.5,  0.5, -0.5,  1.0, 1.0,

        # Top face
        0.5,  0.5,  0.5,  1.0, 0.0,
        -0.5,  0.5,  0.5,  0.0, 0.0,
        -0.5,  0.5, -0.5,  0.0, 1.0,
        0.5,  0.5, -0.5,  1.0, 1.0,

        # Bottom face
        -0.5, -0.5,  0.5,  0.0, 0.0,
        0.5, -0.5,  0.5,  1.0, 0.0,
        0.5, -0.5, -0.5,  1.0, 1.0,
        -0.5, -0.5, -0.5,  0.0, 1.0,

        # Right face
        0.5, -0.5,  0.5,  1.0, 0.0,
        0.5, -0.5, -0.5,  0.0, 0.0,
        0.5,  0.5, -0.5,  0.0, 1.0,
        0.5,  0.5,  0.5,  1.0, 1.0,

        # Left face
        -0.5, -0.5, -0.5,  0.0, 0.0,
        -0.5, -0.5,  0.5,  1.0, 0.0,
        -0.5,  0.5,  0.5,  1.0, 1.0,
        -0.5,  0.5, -0.5,  0.0, 1.0
    ], dtype=np.float32)

    indices = np.array([
        0,  1,  2,  2,  3,  0,
        4,  5,  6,  6,  7,  4,
        8,  9, 10, 10, 11,  8,
        12, 13, 14, 14, 15, 12,
        16, 17, 18, 18, 19, 16,
        20, 21, 22, 22, 23, 20
    ], dtype=np.uint32)

    # Loop until the user closes the window
    while not glfw.window_should_close(window):
        # Render here, e.g. using pyOpenGL

        # Swap front and back buffers
        glfw.swap_buffers(window)

        # Poll for and process events
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()