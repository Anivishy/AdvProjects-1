import pygame, sys, random
from pygame.locals import *
pygame.init()

#colors
GREY = (255, 255, 255)

#window init
background_color = (0,0,0)
FPS =  60
fps_clock = pygame.time.Clock()
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500 
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Hangman')

#font init
font = pygame.font.SysFont('arial', 50)

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
    print("Test")
    pygame.draw.line(WINDOW, GREY, (0,0), (0,0), 20)
   

running = True
target_word = pick_word()
print(target_word)
hangman_draw_init()
while running:    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            letter = event.unicode
                       
        if event.type == pygame.QUIT:
            running = False
            

            