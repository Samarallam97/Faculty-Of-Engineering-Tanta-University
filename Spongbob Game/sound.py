import pygame
pygame.init()
pygame.mixer.init()

###################################################
############## Load sound #########################
###################################################

collision_sound = pygame.mixer.Sound("sounds/collect.mp3")
win_sound = pygame.mixer.Sound("sounds/win..wav")
lose_sound = pygame.mixer.Sound("sounds/loss..mp3")
fish_sound = pygame.mixer.Sound("sounds/fish.mp3")
sea_sound = pygame.mixer.Sound("sounds/sea..mp3")