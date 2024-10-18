#version 460

layout(location = 0) in vec3 vertices;
layout(location = 1) in vec2 tex_coords;
// layout(location = 2) in vec4 colors;

out vec2 texcoords;
// out vec4 newColor;

uniform mat4 vp;
uniform mat4 model;

void main(){
    gl_Position = vp * model * vec4(vertices, 1.0f);
    texcoords = tex_coords;
    // newColor = colors;
}