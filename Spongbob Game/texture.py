from OpenGL.GL import *
import pygame

######################################################################
###########################texture  function #########################
######################################################################
texture_names = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


def my_init():
    loadTextures()


def texture_setup(texture_image_binary, texture_name, width, height):
    glBindTexture(GL_TEXTURE_2D, texture_name) # activate
 
    # setting of texture
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T,
                    GL_REPEAT)  # GL_MIRRORED_REPEAT , GL_CLAMP_TO_EDGE, GL_CLAMP_TO_BORDER
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST) #GL_LINEAR
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

    glTexImage2D(GL_TEXTURE_2D,
                 0,  # mipmap
                 4,  # Bytes per pixel RGB
                 width, height,
                 0,  # Texture border => no border
                 GL_RGBA,  # RGBA Exactly as in  pygame.image.tostring(image, "RGBA", True)
                 GL_UNSIGNED_BYTE, # 0 => 255 storing RGBA
                 texture_image_binary)  # texture init step [7] : raw data


def loadTextures():
    glEnable(GL_TEXTURE_2D) 
    images = []
    images.append(pygame.image.load("img src/game/road10.jpg"))  # 0
    images.append(pygame.image.load("img src/game/day walls.jpeg"))  # 1
    images.append(pygame.image.load("img src/game/day sky.jpg"))  # 2
    images.append(pygame.image.load("img src/game/finalsh.jpg"))  # 3
    images.append(pygame.image.load("img src/game/fish.jpg"))  # 4
    images.append(pygame.image.load("img src/game/finalraceline.jpg"))  # 5
    images.append(pygame.image.load("img src/start/StartBg.jpg"))  # 6
    images.append(pygame.image.load("img src/end/Loser.png"))  # 7
    images.append(pygame.image.load("img src\end\Backgroung.png"))  # 8
    images.append(pygame.image.load("img src\end\sand.png"))  # 9
    images.append(pygame.image.load("img src\end\Victory.png"))  # 10
    images.append(pygame.image.load("img src/game/road7.jpg"))  # 11
    textures = [pygame.image.tostring(image, "RGBA", True)
                for image in images]

    glGenTextures(len(images), texture_names)

    for i in range(len(images)):
        texture_setup(textures[i],  # binary images
                      texture_names[i],  # identifiers
                      images[i].get_width(),
                      images[i].get_height())

"""
each element in texture => texcel | pixel
texture space : normalized coord (t,s)
01 11
00 10 

texture => use pygame

pygame.image.load => load texture from harddisk to memory => return object from type surfice
pygame.image.tostring => convert this object to string => (serialization process) => gives raw image data

pygame.image.tostring(surface, "RGBA", True) : each color in 4 bytes (alpha) => true => pygame flip the image (normal)
pygame.image.tostring(surface, "RGB", false) : each color in 3 bytes => false => (flipped)

pygame.image.tostring => returns raw image data 

raw image data => flipped & higher quality than compressed images

glGenTextures(number of textures objects, texture_names)
take number of textures objects &  texture names
(new)

activate a specific image :

glBindTexture(GL_TEXTURE_2D, texture_names[2])
glBindTexture(texture type,texture_name )

glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
glTexParameterf(texture type ,texture parameter , value of parameter )
works automatocally on the last activated texture


GL_TEXTURE_WRAP_S :  GL_REPEAT => repeat the image in s 

GL_TEXTURE_WRAP_S :  GL_CLAMP=> lengthen the image in s  

GL_TEXTURE_WRAP_T :  GL_REPEAT => repeat the image in t

GL_TEXTURE_WRAP_T :  GL_CLAMP=> lengthen the image in t 

GL_CLAMP : repeat the last coloumn of pixcels in s direction



if number of texcels < number of pixcels => magnification > one texcel covers a group of pixcels
if number of texcels > number of pixcels => minification > a group of texcels is compresed to cover one pixcel

filters types in pygame :
nearest neighbour (point sampling) 
: each pixcel will take the color of the nearest texcel => pixcelled image (but sharper) => number of picells has the samecolor

& bilinear filtering (interpolation) (blury not sharp)

each texcell will take a mixed color of the 4 neighbour texcels
the nearest the texcel , the bigger the percentage that take => so there is no two pixcels that take the same color

glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST) : texcels > pixcels
glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST) : texcels < pixcels

the more the texture is scaled down the more the distortion effect is

mip maping

glTexImage2D :

"""