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

word_file = open("words.txt", "r")

wordlist = word_file.readlines()

def pick_word():
    return wordlist[random.randint(0, len(wordlist))]

running = True
while running:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False
            