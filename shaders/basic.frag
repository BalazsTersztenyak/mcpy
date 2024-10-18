#version 460

in vec2 texcoords;
// in vec4 newColor;

out vec4 outColor;

uniform sampler2D sampTexture;

void main(){
    outColor = texture(sampTexture, texcoords); // * newColor;
    // outColor = newColor;
}