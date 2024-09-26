from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
from variables import *
from texture import *
from demo import *
from sound import *

x_player, z_player = -2.5, -0.5
color = 1


###################################################
############## draw functions #####################
###################################################
def drawLicense():
    glColor3d(1, 1, 1)
    glLoadIdentity()

    glBindTexture(GL_TEXTURE_2D, texture_names[10])  # 10
    glBegin(GL_QUADS)
    glTexCoord2f(0, 1)
    glVertex3d(-3, 2, -2)

    glTexCoord2f(1, 1)
    glVertex3d(3, 2, -2)

    glTexCoord2f(1, 0)
    glVertex3d(3, -2, -2)

    glTexCoord2f(0, 0)
    glVertex3d(-3, -2, -2)
    glEnd()


def drawBackgroung():
    glBindTexture(GL_TEXTURE_2D, texture_names[8])  # 8
    glBegin(GL_QUADS)
    glTexCoord2f(0, 1)
    glVertex3d(-6, 4, -4)

    glTexCoord2f(1, 1)
    glVertex3d(6, 4, -4)

    glTexCoord2f(1.0, 0)
    glVertex3d(6, -4, -4)

    glTexCoord2f(0, 0)
    glVertex3d(-6, -4, -4)

    glEnd()

    glBindTexture(GL_TEXTURE_2D, texture_names[9])  # 9

    glBegin(GL_QUADS)
    glTexCoord2f(0, 1)
    glVertex3d(-6, -2, -3.5)

    glTexCoord2f(1, 1)
    glVertex3d(-6, -4, -3.5)

    glTexCoord2f(1.0, 0)
    glVertex3d(6, -4, -3.5)

    glTexCoord2f(0, 0)
    glVertex3d(6, -1.6, -3.5)

    glEnd()


def drawWin(INTER_FRAMES=0):
    global x_player, z_player, color
    glEnable(GL_DEPTH_TEST)
    glLoadIdentity()
    reposition_camera()
    glClearColor(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glColor3f(color, color, color)

    drawBackgroung()

    glPushMatrix()
    glBindTexture(GL_TEXTURE_2D, -1)

    glTranslate(x_player, -1.3, -2)
    glRotate(90, 0, 1, 0)
    glScale(0.5, 0.5, 0.5)
    get_model("models\FEEPK5E0CZV6F0ZJTQYFDZ3JP.obj").render()

    glPopMatrix()
    glBindTexture(GL_TEXTURE_2D, -1)

    x_player += 0.007
    z_player += 0.001
    color -= 0.001

    if color <= 0:
        win_sound.play()
        drawLicense()

    glutSwapBuffers()


#################################################
############## gl functions #####################
#################################################
def reposition_camera():
    gluLookAt(0, 0, 0,  # eye
              0, 0, -4,  # center
              0, 1, 0)  # up vector


def init_projection():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(90, 1000 / 700, 0.1, 30)
    glMatrixMode(GL_MODELVIEW)


###################################################
############## timer functions ####################
###################################################
def win_timer(v):
    drawWin(v % INTER_FRAMES)
    glutTimerFunc(INTER_INTERVAL, win_timer, v + 1)


###################################################
############## main functions #####################
###################################################
def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(1000, 700)
    glutCreateWindow(b"Win")
    my_init()
    init_projection()
    glutDisplayFunc(drawWin)
    glutTimerFunc(INTER_INTERVAL, win_timer, 1)

    glutMainLoop()


if __name__ == "__main__":
    main()
