import pyglet  # type: ignore
from pyglet.graphics.shader import Shader, ShaderProgram  # type: ignore
from pyglet.math import Vec3, Mat4  # type: ignore
import pyglet.gl as gl  # type: ignore
from pyglet.graphics import Batch  # type: ignore
# import math

class MyWindow(pyglet.window.Window):
    def __init__(self) -> None:
        """Initializes the window and sets up the shader."""
        super().__init__(resizable=True)

        self.set_size(800, 600)
        self.set_caption("Test window")

        self.set_location(100, 100)

        self.batch = Batch()

        self.build_shader("basic")

    def on_draw(self) -> None:
        self.clear()    # window.clear()
        self.batch.draw()   # window.batch.draw()

    def on_resize(self, width: int, height: int) -> None:
        gl.glViewport(0, 0, width, height)

        proj_mat = Mat4.perspective_projection(aspect=width/height, 
                                               z_near=0.1, z_far=100, 
                                               fov=60)
        vp = proj_mat @ self.view_mat
        self.shader['vp'] = vp


    def build_shader(self, shader_name: str) -> None:
        """Builds the shader program from vertex and fragment shader files."""
        with open(f"shaders/{shader_name}.vert", "r") as f:
            vert_src = f.read()

        with open(f"shaders/{shader_name}.frag", "r") as f:
            frag_src = f.read()

        vert_src = Shader(vert_src, 'vertex')
        frag_src = Shader(frag_src, 'fragment')

        self.shader = ShaderProgram(vert_src, frag_src)
        # self.shader.bind()

        # self.view_mat = Mat4.from_translation(Vec3(0, 0, -2))
        self.view_mat = Mat4.look_at(Vec3(0, 0, 3), Vec3(0, 0, 0), Vec3(0, 1, 0))

        proj_mat = Mat4.perspective_projection(fov=60, aspect=800 / 600, 
                                               z_near=0.1, z_far=100)
        
        vp = proj_mat @ self.view_mat

        self.shader['vp'] = vp

        self.translate_mat = Mat4.from_translation(Vec3(0, 0, 0))
        self.angle = 0
        # rotate_mat = Mat4.from_rotation(1, Vec3(0, 1, 0))
        self.scale_mat = Mat4.from_scale(Vec3(1, 1, 1))

        # model_mat = translate_mat @ rotate_mat# @ scale_mat
        # self.shader['model'] = model_mat

        vertices  = [
            -0.5, -0.5, 0.5,
            -0.5, 0.5, 0.5,
            0.5, 0.5, 0.5,
            0.5, -0.5, 0.5

            # -0.5, -0.5, -0.5,
            # -0.5, 0.5, -0.5,
            # 0.5, 0.5, -0.5,
            # 0.5, -0.5, -0.5
        ]

        # vertices = [v * 100 for v in vertices]

        # colors = [
        #     1, 0, 0, 1,
        #     0, 1, 0, 1,
        #     0, 0, 1, 1,
        #     1, 1, 1, 1

            # 0, 0, 1, 1,
            # 1, 1, 1, 1,
            # 1, 0, 0, 1,
            # 0, 1, 0, 1
        # ]

        indices = [
            0, 1, 2, 2, 3, 0#, # front
            # 4, 5, 6, 6, 7, 4, # back
            # 0, 1, 5, 5, 4, 0, # left
            # 1, 2, 6, 6, 5, 1, # top
            # 2, 3, 7, 7, 6, 2, # right
            # 3, 0, 4, 4, 7, 3  # bottom
        ]

        self.vertex_list = self.shader.vertex_list_indexed(
                                        len(vertices) // 3, 
                                        gl.GL_TRIANGLES, 
                                        batch=self.batch, 
                                        indices=indices,
                                        vertices=('f', vertices),
                                        # colors=('f', colors),
                                        tex_coords=('f', [0, 0, 0, 1, 1, 1, 1, 0])
                                        )
        
        self.grass = pyglet.image.load('grass_side.png')
        self.texture = self.grass.get_texture()
        

        # self.shader['sampTexture'] = self.texture
        
    def update(self, dt: float) -> None:
        """Updates the model matrix and applies rotation."""
        # self.angle += dt

        rotate_mat_y = Mat4.from_rotation(self.angle, Vec3(0, 1, 0))
        rotate_mat_x = Mat4.from_rotation(self.angle, Vec3(1, 0, 0))
        model_mat = self.translate_mat @ rotate_mat_y @ rotate_mat_x @ self.scale_mat

        self.shader['model'] = model_mat

def main() -> None:
    window = MyWindow()
    gl.glEnable(gl.GL_DEPTH_TEST)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_NEAREST)
    gl.glBlendFunc(gl.GL_SRC_ALPHA, gl.GL_ONE_MINUS_SRC_ALPHA)

    pyglet.clock.schedule_interval(window.update, 1/60)

    pyglet.app.run()

if __name__ == "__main__":
    main()