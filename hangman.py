import pygame, sys, random
from pygame.locals import *
pygame.init()

background_color = (0,0,0)

FPS =  60
fps_clock = pygame.time.Clock()

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300
 
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Hangman')
