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

#mouse init
LEFT_CLICK = (1,0,0)
RIGHT_CLICK = (0,0,1)

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
temp_wordlist = word_file.readlines()
wordlist = []
for i in range(len(temp_wordlist)):
    wordlist.append(temp_wordlist[i].strip("\n"))
print(wordlist)
#wordlist functions
def pick_word_esasy():
    word =  wordlist[random.randint(0, len(wordlist) - 1)] 
    while len(word) > 5:
        word =  wordlist[random.randint(0, len(wordlist) - 1)]      
    return word

def pick_word_hard():
    word =  wordlist[random.randint(0, len(wordlist) - 1)] 
    while len(word) <= 5:
        word =  wordlist[random.randint(0, len(wordlist) - 1)]      
    return word


def check_word(letter :str, word :str):    
    if letter in word:
        return True
    
#hangman drawing
def hangman_draw_init():
    #pygame.draw.line(surface, GREY, (25,400), (200,400), 10) (template)
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
        pygame.draw.line(surface, BLUE, (25,400), (200,400), 10) #platform
    elif errors == 2:
        pygame.draw.line(surface, BLUE, (50,400), (50,100), 10) #post
    elif errors == 3:
        pygame.draw.line(surface, BLUE, (25,100), (150,100), 10) #top
    elif errors == 4:
        pygame.draw.line(surface, BLUE, (125,100), (125,150), 10) #rope
    elif errors == 5:
        pygame.draw.circle(surface, BLUE, (125, 180), 30, 3) #head
    elif errors == 6:
        pygame.draw.line(surface, BLUE, (125, 210), (125, 300), 3) #body
    elif errors == 7:
        pygame.draw.line(surface, BLUE, (125, 210), (75, 250), 3) #left hand
    elif errors == 8:
        pygame.draw.line(surface, BLUE, (125, 210), (175, 250), 3) #right hand
    elif errors == 9:
        pygame.draw.line(surface, BLUE, (125, 300), (75, 350), 3) #left leg
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
        
def main():
    running = True
    difficulty = 0
    home_screen()
    #loop for home screen, allows user to choose difficulty
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            elif event.type == MOUSEBUTTONDOWN:
                #easy difficulty
                if(pygame.mouse.get_pos()[0] >= 215 and\
                pygame.mouse.get_pos()[1] >= 225 and\
                pygame.mouse.get_pos()[0] <= 285 and\
                pygame.mouse.get_pos()[1] <= 270
                ):
                    difficulty = 1
                    running = False
                    break

                #hard difficulty
                if(pygame.mouse.get_pos()[0] >= 215 and\
                pygame.mouse.get_pos()[1] >= 310 and\
                pygame.mouse.get_pos()[0] <= 285 and\
                pygame.mouse.get_pos()[1] <= 355
                ):                 
                    difficulty = 2
                    running = False
                    break

        if (difficulty!= 0):
            surface.fill(BLACK)
        
        pygame.display.update()
        pygame.time.Clock().tick(60)

    target_word = ""
    if difficulty == 1:
        target_word = pick_word_esasy()
    else:
        target_word = pick_word_hard()

    print(target_word)

    dash_list = []
    for i in range(len(target_word)):
        dash_list.append("-")

    #default vars
    errors = 0
    last_input = ""
    game = True
    Off = 0
    cur_word = ""

    #timer setup
    init_time = 0
    start_time = time.time()
    surface.blit(font_big.render("Time:",True,WHITE),(300,10))
    
    #word display setup
    dashes = font_big.render("".join(dash_list),True,WHITE)
    dash_rect = dashes.get_rect()
    dash_rect.center = (350,250)
    surface.blit(dashes, dash_rect)
    surface.blit(pygame.font.Font("freesansbold.ttf",15).render("1 To Quit",True,WHITE),(20,10))
    
    #main game loop
    while game:
        hangman_draw(errors)
        cur_time = time.time()
        if int(cur_time) - int(start_time) == 1:
            pygame.draw.rect(surface,BLACK,(385,0,100,50))
            init_time = init_time + 1 
            timer = font_big.render(str(init_time),True,WHITE)
            surface.blit(timer, (400,10))
            start_time = time.time()

        for event in pygame.event.get():
            #quit game
            if event.type == pygame.QUIT:
                game = False
            
            elif event.type == KEYDOWN:
                #user inputs letter
                last_input = event.key
                pygame.draw.rect(surface,BLACK,(220,200,280,100))
                pygame.draw.rect(surface,BLACK,(260,50,200,100))
                #check for if it is a valid input (a letter)
                if re.search("[a-z]",chr(event.key)):
                    #check for if guess is in the word
                    if ((chr(event.key).upper() in target_word) or (chr(event.key).lower() in target_word)):
                        for i in range(len(target_word)):
                            if ((target_word[i] == (event.unicode).upper()) or (target_word[i] == (event.unicode).lower())):
                                dash_list[i] = target_word[i]
                            
                    else:
                        #adds one to errors, will be used to update the hang man
                        errors += 1
                    
                    #re-renders the dashes
                    dashes = font_big.render("".join(dash_list),True,WHITE)
                    dash_rect = dashes.get_rect()
                    dash_rect.center = (350,250)
                    surface.blit(dashes, dash_rect)

                else:
                    #if the user chooses to quit the game, ask for confirmation
                    if (event.unicode == "1"):
                        surface.blit(font_big.render("EXIT?",True,RED),(340,220))
                        surface.blit(font_small.render("Yes",True,BLUE),(340,270))
                        surface.blit(font_small.render("No",True,BLUE),(415,270))

                    else:
                        #display "invalid input"
                        Input = font_small.render("INVALID INPUT",True,RED)
                        InputRect = Input.get_rect()
                        InputRect.center = (350,100)
                        surface.blit(Input, InputRect)
                        surface.blit(dashes,dash_rect)

            elif event.type == KEYUP:
                pygame.draw.rect(surface,BLACK,(260,50,200,100))

            elif event.type == MOUSEBUTTONDOWN:
                #turn users choice (yes or no to quit) green
                if (last_input == 49):
                    if (pygame.mouse.get_pressed() == LEFT_CLICK):
                        if (pygame.mouse.get_pos()[0] > 340 and\
                            pygame.mouse.get_pos()[1] > 270 and\
                            pygame.mouse.get_pos()[0] < 385 and\
                            pygame.mouse.get_pos()[1] < 285):
                            pygame.draw.rect(surface,BLACK,(340,270,35,25)) #hide yes
                            surface.blit(font_small.render("Yes",True,GREEN),(340,270))

                        elif (pygame.mouse.get_pos()[0] > 415 and\
                            pygame.mouse.get_pos()[1] > 270 and\
                            pygame.mouse.get_pos()[0] < 450 and\
                            pygame.mouse.get_pos()[1] < 285):
                            pygame.draw.rect(surface,BLACK,(415,270,35,25)) 
                            surface.blit(font_small.render("No",True,GREEN),(415,270))
            
            elif event.type == MOUSEBUTTONUP:
                #quit the game (yes)
                if (last_input == 49):
                    if (pygame.mouse.get_pos()[0] > 340 and\
                    pygame.mouse.get_pos()[1] > 270 and\
                    pygame.mouse.get_pos()[0] < 385 and\
                    pygame.mouse.get_pos()[1] < 285):
                        game = False
                        pygame.quit()
                        sys.exit()
                        break

                    #continue game (no)
                    elif (pygame.mouse.get_pos()[0] > 415 and\
                        pygame.mouse.get_pos()[1] > 270 and\
                        pygame.mouse.get_pos()[0] < 450 and\
                        pygame.mouse.get_pos()[1] < 285):
                        pygame.draw.rect(surface,BLACK,(415,270,35,25)) #hide no
                        surface.blit(font_small.render("No",True,GREEN),(415,270))
                        pygame.draw.rect(surface,BLACK,(300,200,200,100)) #hide exit, yes,no

                        dashes = font_big.render("".join(dash_list),True,BLACK)
                        dash_list = dashes.get_rect()
                        dash_rect.center = (400,250)
                        surface.blit(dashes,dash_rect)

                        last_input = ""

                    else:
                        pygame.draw.rect(surface,WHITE,(340,270,35,25)) 
                        surface.blit(font_small.render("Yes",True,BLUE),(340,270))
                        pygame.draw.rect(surface,WHITE,(415,270,35,25)) 
                        surface.blit(font_small.render("No",True,BLUE),(415,270))

        if (errors == 10):
            #if the users has lost (hangman is fully collored in)
            surface.fill(BLACK)
            hangman_draw(errors)
            game_over = font_big.render("GAME OVER",True,RED)
            game_over_rect = game_over.get_rect()
            game_over_rect.center = (400,250)
            surface.blit(game_over,game_over_rect)
            Off = 1

            #reveal the word
            Word = font_small.render("The word was:",True,RED)
            WordRect = Word.get_rect()
            WordRect.center = (400,300)
            surface.blit(Word,WordRect)

            Word2 = font_big.render(target_word,True,RED)
            Word2Rect = Word2.get_rect()
            Word2Rect.center = (400,335)
            surface.blit(Word2,Word2Rect)

        elif (target_word == "".join(dash_list)):
            print("test2")
            surface.fill(BLACK)
            congrats = font_big.render("CONGRATS, YOU WON",True,GREEN)
            congrats_rect = congrats.get_rect()
            congrats_rect.center = (250,220)
            surface.blit(congrats,congrats_rect)

            #reveal the word
            Word = font_small.render("The word was:",True,WHITE)
            WordRect = Word.get_rect()
            WordRect.center = (250,250)
            surface.blit(Word,WordRect)

            Word2 = font_big.render(target_word,True,WHITE)
            Word2Rect = Word2.get_rect()
            Word2Rect.center = (250,285)
            surface.blit(Word2,Word2Rect)
            
            Off = 1          

        pygame.display.update()
        pygame.time.Clock().tick(60) 
        
        if (Off == 1):
            #5 second delay before closing game window
            time.sleep(5)
            pygame.quit()
            sys.exit()   

main()         
                                



    



        # elif event.type == pygame.KEYDOWN:
        #     letter = event.unicode
        #     print(event.unicode)
                       
        
            



            