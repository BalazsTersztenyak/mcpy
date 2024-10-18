from pyglet.graphics import shader

def get_program(shader_name):
        with open(f"shaders/{shader_name}.vert", 'r') as f:
            vertex_source = f.read()

        with open(f"shaders/{shader_name}.frag", 'r') as f:
            fragment_source = f.read()

        vert_shader = shader.Shader(vertex_source, 'vertex')
        frag_shader = shader.Shader(fragment_source, 'fragment')
        return shader.ShaderProgram(vert_shader, frag_shader)
