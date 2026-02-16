"""This module provides a function to load and compile vertex and fragment shaders 
from files, and create a shader program that can be used in rendering. 
"""
from pyglet.graphics import shader

def get_program(shader_name: str):
    """Loads shader with name shader_name

    Args:
        shader_name (str): The base name of the shader (without extension)

    Returns:
        shader.ShaderProgram: The compiled shader program
    """
    with open(f"shaders/{shader_name}.vert", 'r', encoding='utf-8') as f:
        vertex_source = f.read()

    with open(f"shaders/{shader_name}.frag", 'r', encoding='utf-8') as f:
        fragment_source = f.read()

    vert_shader = shader.Shader(vertex_source, 'vertex')
    frag_shader = shader.Shader(fragment_source, 'fragment')
    return shader.ShaderProgram(vert_shader, frag_shader)
