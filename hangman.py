import pygame, sys, random, time, re
from pygame.locals import *

pygame.init()

#colors
GREY = (128, 128, 128)
WHITE = (225, 225, 225)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DARK_GREEN = (0, 181, 3)
DARK_RED = (171, 2, 2)

#window init
FPS =  60
fps_clock = pygame.time.Clock()
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500 
surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Hangman')

#font init
font_big = pygame.font.SysFont('arial', 40)
font_small = pygame.font.SysFont('arial', 20)

#wordlist init
word_file = open("words.txt", "r")
wordlist = word_file.readlines()

#wordlist functions
def pick_word_esasy():
    return wordlist[random.randint(0, len(wordlist) - 1)]

def pick_word_hard():
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
    pygame.draw.line(surface, GREY, (125, 300), (75, 350), 3) #left leg
    pygame.draw.line(surface, GREY, (125, 300), (175, 350), 3) #right leg
    
def hangman_draw(errors: int):
    if errors == 0:
        hangman_draw_init()
    elif errors == 1:
        hangman_draw_init()
        pygame.draw.line(surface, BLUE, (25,400), (200,400), 10) #platform
    elif errors == 2:
        hangman_draw_init()
        pygame.draw.line(surface, BLUE, (50,400), (50,100), 10) #post
        if errors > 1:
            hangman_draw(errors - 1)
    elif errors == 3:
        hangman_draw_init()
        pygame.draw.line(surface, BLUE, (25,100), (150,100), 10) #top
        if errors > 1:
            hangman_draw(errors - 1)
    elif errors == 4:
        hangman_draw_init()
        pygame.draw.line(surface, BLUE, (125,100), (125,150), 10) #rope
        if errors > 1:
            hangman_draw(errors - 1)
    elif errors == 5:
        hangman_draw_init()
        pygame.draw.circle(surface, BLUE, (125, 180), 30, 3) #head
        if errors > 1:
            hangman_draw(errors - 1)
    elif errors == 6:
        hangman_draw_init()
        pygame.draw.line(surface, BLUE, (125, 210), (125, 300), 3) #body
        if errors > 1:
            hangman_draw(errors - 1)
    elif errors == 7:
        hangman_draw_init()
        pygame.draw.line(surface, BLUE, (125, 210), (75, 250), 3) #left hand
        if errors > 1:
            hangman_draw(errors - 1)
    elif errors == 8:
        hangman_draw_init()
        pygame.draw.line(surface, BLUE, (125, 210), (175, 250), 3) #right hand
        if errors > 1:
            hangman_draw(errors - 1)
    elif errors == 9:
        hangman_draw_init()
        pygame.draw.line(surface, BLUE, (125, 210), (75, 250), 3) #left leg
        if errors > 1:
            hangman_draw(errors - 1)
    elif errors == 10:
        #game over
        pygame.draw.line(surface, RED, (25,400), (200,400), 10) #platform
        pygame.draw.line(surface, RED, (50,400), (50,100), 10) #post
        pygame.draw.line(surface, RED, (25,100), (150,100), 10) #top
        pygame.draw.line(surface, RED, (125,100), (125,150), 10) #rope
        pygame.draw.circle(surface, RED, (125, 180), 30, 3) #head
        pygame.draw.line(surface, RED, (125, 210), (125, 300), 3) #body
        pygame.draw.line(surface, RED, (125, 210), (75, 250), 3) #left hand
        pygame.draw.line(surface, RED, (125, 210), (175, 250), 3) #right hand
        pygame.draw.line(surface, RED, (125, 300), (75, 350), 3) #left leg
        pygame.draw.line(surface, RED, (125, 300), (175, 350), 3) #right leg

def home_screen():
    #title
    text_title = font_big.render("HANGMAN", True, WHITE, BLACK)
    textbox_title = text_title.get_rect()
    textbox_title.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 4)
    #name
    text_name = font_small.render("By: Ani", True, WHITE, BLACK)
    textbox_name = text_name.get_rect()
    textbox_name.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 3.2)
    #easy button
    text_easy = font_big.render("Easy", True, WHITE, DARK_GREEN)
    textbox_easy = text_easy.get_rect()
    textbox_easy.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
    #hard button
    text_hard = font_big.render("Hard", True, WHITE, RED)
    textbox_hard = text_hard.get_rect()
    textbox_hard.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 1.5)
    surface.blit(text_title, textbox_title)
    surface.blit(text_name, textbox_name)
    surface.blit(text_easy, textbox_easy)
    surface.blit(text_hard, textbox_hard)
        
running = True
#target_word = pick_word()
#print(target_word)
surface.fill(BLACK)
#home_screen()
hangman_draw(10)
pygame.display.update() 

while running:
    difficulty = 0  
    errors = 0
    home_screen()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == MOUSEBUTTONDOWN:
            #easy difficulty
            if(pygame.mouse.getpos()[0] > x and
               pygame.mouse.get_post()[1] > y
            ):
                target = pick_word_esasy()


            #hard difficulty
            if(pygame.mouse.getpos()[0] > x and
               pygame.mouse.get_post()[1] > y
            ):
                target = pick_word_hard()

        elif event.type == pygame.KEYDOWN:
            letter = event.unicode
            print(event.unicode)
                       
        
            



            