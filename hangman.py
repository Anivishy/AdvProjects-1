import pygame, sys, random, time, re
from pygame.locals import *

pygame.init()

#colors
GREY = (128, 128, 128)
WHITE = (225, 225, 225)
BLACK = (0, 0, 0)

#window init
FPS =  60
fps_clock = pygame.time.Clock()
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500 
surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
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
    
#hangman drawing
def hangman_draw_init():
    #pygame.draw.line(surface, GREY, (25,400), (200,400), 10)
    pygame.draw.line(surface, GREY, (25,400), (200,400), 10) #platform
    pygame.draw.line(surface, GREY, (50,400), (50,100), 10) #post
    pygame.draw.line(surface, GREY, (25,100), (150,100), 10) #top
    pygame.draw.line(surface, GREY, (125,100), (125,150), 10) #rope
    pygame.draw.circle(surface, GREY, (125, 180), 30, 3) #head
    pygame.draw.line(surface, GREY, (125, 210), (125, 300), 3) #body
    pygame.draw.line(surface, GREY, (125, 210), (75, 250), 3) #left hand
    pygame.draw.line(surface, GREY, (125, 210), (175, 250), 3) #right hand
    pygame.draw.line(surface, GREY, (125, 210), (75, 250), 3) #left leg
    pygame.draw.line(surface, GREY, (125, 210), (175, 250), 3) #right right leg  
    
   

running = True


while running:
    difficulty = 0  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == MOUSEBUTTONDOWN:
            #easy difficulty
            if(pygame.mouse.getpos()[0] > x and
               pygame.mouse.get_post()[1] > y
            ):
                pass


            #hard difficulty
            if(pygame.mouse.getpos()[0] > x and
               pygame.mouse.get_post()[1] > y
            ):
                pass

        elif event.type == pygame.KEYDOWN:
            letter = event.unicode
            print(event.unicode)
                       
        
            


target_word = pick_word()
print(target_word)
surface.fill(BLACK)
hangman_draw_init()
pygame.display.update() 
            