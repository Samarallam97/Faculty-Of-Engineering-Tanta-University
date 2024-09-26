"""
Documentation:
    1) Game story:
         Spongebob Driving Test
         It is a game to help Spongebob to get the driver's license and consists of 3 stages,
         First one, which is the beginning of the game, a two-dimensional window to start or end.
         Second one, which is a three-dimensional window,
         in which you collect stars and not injure the fish and the diver.
         The last, consists of two cases winning or losing. 
         If you win, you get the license and exit.
         If you lose, you start again or exit.
         More details:
         When a fish is injured, the speed decreases, and when a star is token, the speed increases.

    2) about us :
    Team 5 from faculty of engineering Tanta university:
    1- Abdelhamed Ragheb Elhafny
    2- Samar Shaaban Ramadan
    3- Salma Waleed Abdulshakoor
    4- Salma Hassan 
    5- Mariam Hassanin Mohammed
    6- Fatma Nasser Ataallah
    7- Menna Ehab Shoman
    8- Mona Muhammad Ayoub
    9- Heba Abdel Moneim Nagy
    10- Nourhan Sameh Fayyad
    11- Habiba Mohammed El-Sharqawi
    12- Mahmoud Kamal El-Sadani

    3) Supervised by Dr/ Mohamed Ali and Eng/ Mohammed El-koumy.

"""
######################################################################
########################### python library ###########################
######################################################################
import sys
import random
import time
import math
import numpy as np

######################################################################
########################### Opengl library ###########################
######################################################################
from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
import pygame

#####################################################################
########################### Game library ###########################
#####################################################################
from texture import *
from variables import *
from Objects import *
import xx_tryWin
from sound import *
from demo import *

######################################################################
########################### Game chracter ############################
######################################################################
player = PLAYER(0, 1.5, -5, 2)
camara1 = Camera(0, 7, 15, 0, 0, -zFar)
string_postion = DRAWSTRING(-X_WIDTH, Y_WIDTH - 2, -3, "L I V E S  : ")

######################################################################
########################## Game status ###############################
######################################################################

next_px = player.x  # feature point
delta_z = 1
delta_x = .45678
states = [0, 1, 2, 3]  # 0 =>  start // 1 => game // 2 => win // 3 => lose
currentstate = 0


#################################################################
###########################GL scene #############################
#################################################################
def init_my_scene():
    glClearColor(0, 0, 0, 0)  # Clear background to white .
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()  # Reset projection matrix.
    gluPerspective(45.0, WIDTH / HEIGHT, zNear,-zFar)
    glMatrixMode(GL_MODELVIEW)


def reposition_camera(inter_frame=0):
    global camara1, player
    # interpolation_factor = inter_frame / (INTER_FRAMES - 1)
    # camara1.ez = next_ce * interpolation_factor + camara1.ez * (1 - interpolation_factor)
    gluLookAt(
        0, 7, camara1.ez,
        # camara1.ex, camara1.ey, camara1.ez,  # eye
        # player.x, player.y, player.z,  # center
        # camara1.cx, camara1.cy, camara1.cz,
        0, 0, camara1.cz,
        0, 1, 0
    )


######################################################################
###########################draw functions ############################
######################################################################
def draw_scene():
    global textureconstant
    zOfFrontWall = zFar
    glPushMatrix()
    # Front image
    glBindTexture(GL_TEXTURE_2D, texture_names[3])
    glColor3ub(225, 255, 255)
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex3f(-X_WIDTH - 5, 0, -zOfFrontWall - 19)
    # -15 , 0 , -850-19
    glTexCoord2f(0, 1)
    glVertex3f(-X_WIDTH - 5, Y_WIDTH, -zOfFrontWall - 19)
    # -15 , 15 , -850-19
    glTexCoord2f(1, 1)
    glVertex3f(X_WIDTH + 5, Y_WIDTH, -zOfFrontWall - 19)
    # 15 , 15 , -850-19
    glTexCoord2f(1, 0)
    glVertex3f(X_WIDTH + 5, 0, -zOfFrontWall - 19)
    # 15 , 0 , -850-19
    glEnd()

    # Roof
    glBindTexture(GL_TEXTURE_2D, texture_names[2])
    glColor3f(1, 1, 1)
    glBegin(GL_QUADS)
    glTexCoord2f(textureconstant, 0)
    glVertex3f(X_WIDTH + 5, Y_WIDTH, 0)

    glTexCoord2f(textureconstant, 1)
    glVertex3f(-X_WIDTH - 5, Y_WIDTH, 0)

    glTexCoord2f(1, 1)
    glVertex3f(-X_WIDTH - 5, Y_WIDTH, -zOfFrontWall - 20)

    glTexCoord2f(1, 0)
    glVertex3f(X_WIDTH + 5, Y_WIDTH, -zOfFrontWall - 20)
    glEnd()

    # Left wall
    glBindTexture(GL_TEXTURE_2D, texture_names[1])  # 1
    glColor3f(1, 1, 1)
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex3f(-X_WIDTH - 5, 0, 0)

    glTexCoord2f(0, 1)
    glVertex3f(-X_WIDTH - 5, Y_WIDTH, 0)

    glTexCoord2f(textureconstant, 1)
    glVertex3f(-X_WIDTH - 5, Y_WIDTH, -zOfFrontWall - 20)

    glTexCoord2f(textureconstant, 0)
    glVertex3f(-X_WIDTH - 5, 0, -zOfFrontWall - 20)
    glEnd()

    # Right wall
    glBindTexture(GL_TEXTURE_2D, texture_names[1])  # 1
    glColor3f(1, 1, 1)
    glBegin(GL_QUADS)

    glTexCoord2f(0, 0)
    glVertex3f(X_WIDTH + 5, 0, 0)

    glTexCoord2f(0, 1)
    glVertex3f(X_WIDTH + 5, Y_WIDTH, 0)

    glTexCoord2f(textureconstant, 1)
    glVertex3f(X_WIDTH + 5, Y_WIDTH, -zOfFrontWall - 20)

    glTexCoord2f(textureconstant, 0)
    glVertex3f(X_WIDTH + 5, 0, -zOfFrontWall - 20)
    glEnd()

    # Ground
    glBindTexture(GL_TEXTURE_2D, texture_names[0])  # 0
    glColor3f(1, 1, 1)
    glBegin(GL_POLYGON)

    glTexCoord2f(0, groundconstant)
    glVertex3d(-X_WIDTH, 0, 0)

    glTexCoord2f(1, groundconstant)
    glVertex3d(X_WIDTH, 0, 0)

    glTexCoord2f(1, 0)
    glVertex3d(X_WIDTH, 0, -zOfFrontWall)

    glTexCoord2f(0, 0)
    glVertex3d(-X_WIDTH, 0, -zOfFrontWall)

    glEnd()

    # final Ground
    glBindTexture(GL_TEXTURE_2D, texture_names[5])  # 5
    glColor3f(1, 1, 1)
    glBegin(GL_POLYGON)

    glTexCoord2f(0, 1)
    glVertex3d(-X_WIDTH, 0, -zOfFrontWall)

    glTexCoord2f(1, 1)
    glVertex3d(X_WIDTH, 0, -zOfFrontWall)

    glTexCoord2f(1, 0)
    glVertex3d(X_WIDTH, 0, -zOfFrontWall - 20)

    glTexCoord2f(0, 0)
    glVertex3d(-X_WIDTH, 0, -zOfFrontWall - 20)

    glEnd()

    # right Ground
    glBindTexture(GL_TEXTURE_2D, texture_names[11])  # 11
    glColor3f(1, 1, 1)
    glBegin(GL_POLYGON)

    glTexCoord2f(0, groundconstant)
    glVertex3d(-X_WIDTH, 0, 0)

    glTexCoord2f(1, groundconstant)
    glVertex3d(-X_WIDTH - 5, 0, 0)

    glTexCoord2f(1, 0)
    glVertex3d(-X_WIDTH - 5, 0, -zOfFrontWall - 20)

    glTexCoord2f(0, 0)
    glVertex3d(-X_WIDTH, 0, -zOfFrontWall - 20)

    glEnd()

    # right Ground
    glBindTexture(GL_TEXTURE_2D, texture_names[11])  # 11
    glColor3f(1, 1, 1)
    glBegin(GL_POLYGON)

    glTexCoord2f(0, groundconstant)
    glVertex3d(X_WIDTH, 0, 0)

    glTexCoord2f(1, groundconstant)
    glVertex3d(X_WIDTH + 5, 0, 0)

    glTexCoord2f(1, 0)
    glVertex3d(X_WIDTH + 5, 0, -zOfFrontWall - 20)

    glTexCoord2f(0, 0)
    glVertex3d(X_WIDTH, 0, -zOfFrontWall - 20)

    glEnd()

    glBindTexture(GL_TEXTURE_2D, -1)
    glPopMatrix()


def drawDiver():
    glPushMatrix()
    glBindTexture(GL_TEXTURE_2D, -1)
    glTranslate(0, 1, -zFar / 2)
    glRotate(-90, 1, 0, 0)
    glScale(0.3, 0.3, 0.3)
    get_model("models/diver/13018_Aquarium_Deep_Sea_Diver_v1_L1.obj").render()
    glPopMatrix()


def initNegativePoints(points):
    for i in range(len(points)):
        glPushMatrix()
        glBindTexture(GL_TEXTURE_2D, texture_names[4])  # 4
        glColor3f(1, 1, 1)
        glTranslatef(points[i][0], points[i][1], points[i][2])
        glRotate(-90, 1, 0, 0)
        glScale(.1, .1, .1)
        get_model("models/fish/12265_Fish_v1_L2.obj").render()
        glBindTexture(GL_TEXTURE_2D, -1)
        glPopMatrix()


def initPositivePoints(points):
    for i in range(len(points)):
        glPushMatrix()
        glColor3f(1, 1, 0)

        glTranslatef(points[i][0], points[i][1], points[i][2])
        glRotate(-90, 1, 0, 0)
        glScale(.4, .4, .4)
        get_model("models/star2/18337_Star_v1.obj").render()

        glPopMatrix()


######################################################################
################# points & its movement  #############################
######################################################################

def DrawPoints():
    global zFar, pointsPlus, pointsMinus
    i = 20
    while i:
        x = random.choice(POSITIONS)
        z = random.randint(-zFar, player.z - 1)
        if (x, 1, z) in pointsMinus or (x, 1, z) in pointsPlus:
            continue
        else:
            pointsPlus.append((x, 1, z))
            i -= 1

    i = 30
    while i:
        x = random.choice(POSITIONS)
        z = random.randint(-zFar, player.z - 1)
        if (x, 1, z) in pointsMinus or (x, 1, z) in pointsPlus:
            continue
        else:
            pointsMinus.append((x, 1, z))
            i -= 1

# list of tuples

def checksign(sign, poi):
    global player, delta_z, pointsPlus, pointsMinus
    if sign == 0: 
        player.live -= 1
        fish_sound.play()
        pointsMinus.remove(poi)
        if delta_z > 1:
            delta_z -= 0.1
    else:
        player.live += 1
        collision_sound.play()
        pointsPlus.remove(poi)
        if delta_z < 1.3:
            delta_z += 0.1

#  (0,0,0) => (1,0,0) , (-1,0,0)
def TestCollision(points, sign):
    global player, zFar, delta_z
    cp = (round(player.x), 1, math.floor(player.z)) # player position
    pncp = (cp[0] + 1, cp[1], cp[2])
    nncp = (cp[0] - 1, cp[1], cp[2])
    
    if (cp) == (0, 1, -zFar / 2):  # diver
        player.live -= player.live
# (0,0,0) => [(1,1,1) , (0,0,0)]
    if cp in points:  # current x postion
        checksign(sign=sign, poi=cp)
    elif pncp in points:  # right x postion
        checksign(sign=sign, poi=pncp)
    elif nncp in points:  # left x postion
        checksign(sign=sign, poi=nncp)


######################################################################
###########################draw text  functions ######################
######################################################################

def drawText(string, inter_frame):
    global string_postion
    glPushMatrix()
    glLineWidth(4)
    glColor3ub(255, 215, 0)  # Yellow Color
    glTranslate(string_postion.x, string_postion.y, string_postion.z) 
    glScale(0.003, 0.003, 0.003)
    string = string.encode()  # conversion from Unicode string to byte string
    for c in string:  # render character by character starting from the origin
        glutStrokeCharacter(GLUT_STROKE_ROMAN, c)
    glLineWidth(2)
    glPopMatrix()


######################################################################
###########################smoth move  functions #####################
######################################################################
def draw_player(inter_frame=0):
    global player, next_px, next_pz, delta_z
    interpolation_factor = inter_frame / (INTER_FRAMES - 1)
    glColor3ub(255, 255, 255)
    player.x = next_px * interpolation_factor + player.x * (1 - interpolation_factor)

    glPushMatrix()
    glTranslate(player.x, player.y, player.z)
    glRotate(180, 0, 1, 0)
    glScale(2.5, 2.5, 2.5)  # scale up
    get_model("models\FEEPK5E0CZV6F0ZJTQYFDZ3JP.obj").render()
    glPopMatrix()


##############################################################
###########################game state 0 ######################
##############################################################
def draw_start():
    global player, currentstate
    lz = round(player.z) + 4 # -5 + 4 => -1
    glBindTexture(GL_TEXTURE_2D, texture_names[6])  # 6
    glPushMatrix()
    glColor3f(1, 1, 1)
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex3f(-X_WIDTH, 0, lz)

    glTexCoord2f(0, 1)
    glVertex3f(-X_WIDTH, Y_WIDTH - 1, lz)

    glTexCoord2f(1, 1)
    glVertex3f(X_WIDTH, Y_WIDTH - 1, lz)

    glTexCoord2f(1, 0)
    glVertex3f(X_WIDTH, 0, lz)
    glEnd()
    glPopMatrix()
    glBindTexture(GL_TEXTURE_2D, -1)


##############################################################
###########################game state 1 ######################
##############################################################
def draw_game(inter_frame=0):
    global next_pz, delta_z, camara1, player, next_ce, next_cc, next_sz, currentstate, string_postion
    glPushMatrix()
    draw_scene()
    drawDiver()
    initNegativePoints(pointsMinus)
    initPositivePoints(pointsPlus)

    glBindTexture(GL_TEXTURE_2D, -1)
    STRING = string_postion.text + str(player.live)
    drawText(STRING, inter_frame=inter_frame)

    draw_player(inter_frame=inter_frame)
    TestCollision(pointsMinus, 0)
    TestCollision(pointsPlus, 1)

    player.z -= delta_z
    camara1.ez -= delta_z
    camara1.cz -= delta_z
    string_postion.z -= delta_z

    if player.live <= 0:
        print("You lose :( ")
        currentstate = 3

    if player.z <= -zFar: # -851 <= -850
        print("GoodGame :D")
        currentstate = 2

    glPopMatrix()


##############################################################
###########################game state 3 ######################
##############################################################
def drawLose():
    global player, currentstate
    lz = round(player.z) + 4
    glBindTexture(GL_TEXTURE_2D, texture_names[7])  # 7
    glPushMatrix()
    glColor3f(1, 1, 1)
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex3f(-X_WIDTH, 0, lz)

    glTexCoord2f(0, 1)
    glVertex3f(-X_WIDTH, Y_WIDTH - 1, lz)

    glTexCoord2f(1, 1)
    glVertex3f(X_WIDTH, Y_WIDTH - 1, lz)

    glTexCoord2f(1, 0)
    glVertex3f(X_WIDTH, 0, lz)
    glEnd()
    glPopMatrix()
    glBindTexture(GL_TEXTURE_2D, -1)


#############################################################
###########################game states ######################
#############################################################
def display(inter_frame=0):
    global next_pz, delta_z, camara1, player, next_ce, next_cc, next_sz, currentstate
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    reposition_camera(inter_frame=inter_frame)
   
    if currentstate == 1:
        draw_game(inter_frame=inter_frame)
    elif currentstate == 0:
        draw_start()
    elif currentstate == 3:
        lose_sound.play()
        drawLose()
    elif currentstate == 2:
        xx_tryWin.drawWin()  # game state 2
    glutSwapBuffers()
    # glDeleteTextures(1 , texture_names + 2) # texture_names : address of 1st tex

####################################################################
#######player keyboard control functions #############################
######################################################################
def keyboard_player(key, m_x, m_y):
    global player, next_px, camara1, next_pz, delta_z, delta_x, next_sz
    if key == GLUT_KEY_LEFT and next_px > -8 and currentstate == 1:
        next_px -= delta_x
    elif key == GLUT_KEY_RIGHT and next_px < 8 and currentstate == 1:
        next_px += delta_x
    # print(player.x, player.y, player.z)


######################################################################
###########################control time  functions ###################
######################################################################
def game_status_control(key, c_x, c_y):
    global currentstate, player, camara1, zFar, string_postion
    if key == b'\x0D' and currentstate in [0, 3]:  # Enter
        print("EnterGame :) Wait a 1s please !")
        player = PLAYER(0, 1.5, -5, 2)
        camara1 = Camera(0, 7, 15, 0, 0, -zFar)
        string_postion = DRAWSTRING(-X_WIDTH, Y_WIDTH - 2, -3, "L I V E S  : ")
        currentstate = 1

    elif key == b'\x1B' and currentstate in [0, 2, 3]:  # ESC
        print("GoodBye :D")
        sys.exit(0)


def game_timer(v):
    if currentstate != 2:
        display(v % INTER_FRAMES)
    else:
        xx_tryWin.init_projection()
        xx_tryWin.drawWin(v % INTER_FRAMES)
    glutTimerFunc(INTER_INTERVAL, game_timer, v + 1)


##############################################################
###########################main  functions ###################
##############################################################
def main():
    glutInit()
    glutInitWindowSize(WIDTH, HEIGHT)
    glutInitWindowPosition(400, 50)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutCreateWindow(b"Spongebob Test Drive")
    my_init()
    sea_sound.play(-1)
    glutDisplayFunc(display)
    glutTimerFunc(INTER_INTERVAL, game_timer, 1)
    glutSpecialFunc(keyboard_player)
    glutKeyboardFunc(game_status_control)
    init_my_scene()
    glutMainLoop()


if __name__ == "__main__":
    DrawPoints()  # make points
    main()
