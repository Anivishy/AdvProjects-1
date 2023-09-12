import pygame, sys, random, time, re
from pygame.locals import *

pygame.init()

#window init
background_color = (0,0,0)
FPS =  60
fps_clock = pygame.time.Clock()
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300 
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
pygame.display.set_caption('Hangman')

#font init
font_big = pygame.font.SysFont('arial', 40)
font_small = pygame.font.SysFont('arial', 30)

#wordlist init
word_file = open("words.txt", "r")
wordlist = word_file.readlines()

#wordlist functions
def pick_word():
    return wordlist[random.randint(0, len(wordlist) - 1)]

def check_word(letter :str, word :str):    
    if letter in word:
        return True
   

running = True
target_word = pick_word()
print(target_word)
while running:    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            letter = event.unicode
                       
        if event.type == pygame.QUIT:
            running = False
            

            