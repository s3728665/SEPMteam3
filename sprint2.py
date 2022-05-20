##SEPM GROUP-3 WORDLE APP USING PYGAME
##references:
# https://github.com/learntocodeGCSE/wordle
#https://www.youtube.com/watch?v=SyWeex-S6d0&t=1810s&ab_channel=Pixegami
#https://www.youtube.com/watch?v=ZpYZ7Y5Vgd8&t=1231s&ab_channel=LearntoCodeGCSE

from lib2to3.pgen2.token import LEFTSHIFT
import random, pygame, sys
from pygame.locals import *
from sklearn.utils import column_or_1d
pygame.init()

## default colour scheme / RGB
white = (255,255,255)
yellow = (198,181,102)
#dark grey
grey = (58,58,60)
black = (18,18,20)
green=(121,168,104)
lightGreen=(153,255,204)
lred = (245,80,80)
## Colour blind/ high contrast colour scheme
### light blue = correct letter, wrong placing
###  orange = correct letter, correct placement
blue = (132,193,250)
orange = (245,121,59)
#light and dark grey
lgrey = (121,125,129)
##light grey frame for ligght mode
lgrey2 = (218,218,218)

##actual font for original wordle is Neue Helvetica 75 Bold
font = pygame.font.SysFont("Helvetica neue bold", 55)
bigFont = pygame.font.SysFont("Helvetica neue bold", 80)

youWin = bigFont.render("You Won!",       True, lred)
youLose = bigFont.render("You Lost!",     True, lred)
playAgain = bigFont.render("Play Again?", True, lred)

##colour change

##dark mode
def checkGuess(turns, word, userGuess, window):
    renderList = ["","","","",""]
    spacing = 0
    guessColourCode = [grey,grey,grey,grey,grey]

    for x in range(0,5):
        if userGuess[x] in word:
            guessColourCode[x] = yellow

        if word[x] == userGuess[x]:
            guessColourCode[x] = green

    list(userGuess)

    for x in range(0,5):
        renderList[x] = font.render(userGuess[x], True, white)
        ##frames (50+(x*76), 50+(y*76), 70, 70),2)
        pygame.draw.rect(window, guessColourCode[x], pygame.Rect(50 +spacing, 50+ (turns*76), 70, 70))
        window.blit(renderList[x], (70 + spacing, 70 + (turns*76)))
        spacing+=76

    if guessColourCode == [green,green,green,green,green]:
        return True

def checkGuessCB(turns, word, userGuess, window):
    renderList = ["","","","",""]
    spacing = 0
    guessColourCode = [grey,grey,grey,grey,grey]

    for x in range(0,5):
        if userGuess[x] in word:
            guessColourCode[x] = blue

        if word[x] == userGuess[x]:
            guessColourCode[x] = orange

    list(userGuess)

    for x in range(0,5):
        renderList[x] = font.render(userGuess[x], True, white)
        ##frames (50+(x*76), 50+(y*76), 70, 70),2)
        pygame.draw.rect(window, guessColourCode[x], pygame.Rect(50 +spacing, 50+ (turns*76), 70, 70))
        window.blit(renderList[x], (70 + spacing, 70 + (turns*76)))
        spacing+=76

    if guessColourCode == [orange,orange,orange,orange,orange]:
        return True

def checkGuessLight(turns, word, userGuess, window):
    renderList = ["","","","",""]
    spacing = 0
    guessColourCode = [lgrey,lgrey,lgrey,lgrey,lgrey]

    for x in range(0,5):
        if userGuess[x] in word:
            guessColourCode[x] = yellow

        if word[x] == userGuess[x]:
            guessColourCode[x] = green

    list(userGuess)

    for x in range(0,5):
        renderList[x] = font.render(userGuess[x], True, white)
        ##frames (50+(x*76), 50+(y*76), 70, 70),2)
        pygame.draw.rect(window, guessColourCode[x], pygame.Rect(50 +spacing, 50+ (turns*76), 70, 70))
        window.blit(renderList[x], (70 + spacing, 70 + (turns*76)))
        spacing+=76

    if guessColourCode == [green,green,green,green,green]:
        return True

def main():
    file = open("wordList.txt","r")
    wordList = file.readlines()
    word = wordList[random.randint(0, len(wordList)-1)].upper()

    ##background colour test
    #global bcolour
    #bcolour = white

    height = 600
    width = 500

    FPS = 30
    clock = pygame.time.Clock()

    window = pygame.display.set_mode((width, height))
    ##background colopur default white
    bg = window.fill(white)

    guess = ""

    print(word)

    for x in range(0,5):
        for y in range(0,6):
            pygame.draw.rect(window, lgrey2, pygame.Rect(50+(x*76), 50+(y*76), 70, 70),2)

    pygame.display.set_caption("Wordle")

    turns = 0
    win = False

    

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.exit()
                sys.exit()
            
            

            if event.type == pygame.KEYDOWN:
                guess+=event.unicode.upper()

                if event.key == K_RETURN and win == True:
                    main()

                if event.key == K_RETURN and turns == 6:
                    main()

                if event.key == pygame.K_BACKSPACE or len(guess) > 5:
                    guess = guess[:-1]

                # if event.key == K_RETURN and len(guess) > 4:
                #     win = checkGuess(turns, word, guess, window)
                #     turns+=1
                #     guess = ""
                #     window.fill(black,(0,500, 500, 200))
               
                ##
                if event.key == K_RETURN and len(guess) > 4:
                    k = pygame.key.get_pressed()
                    ##hold L shsift and type soemthing then enter to enter dark mode
                    ##dark mode L shift
                    if k[pygame.K_LSHIFT]:
                        win = checkGuess(turns, word, guess, window)
                        bg = window.fill(black)
                        turns+=1
                        guess = ""
                        #window.fill(white,(0,500, 500, 200))
                        guess = ""

                        print(word)

                        for x in range(0,5):
                            for y in range(0,6):
                                pygame.draw.rect(window, grey, pygame.Rect(50+(x*76), 50+(y*76), 70, 70),2)

                        pygame.display.set_caption("Wordle")

                        turns = 0
                        win = False
                        #window.fill(black,(0,500, 500, 200))
                        ##chin colour 
                        cc = window.fill(black,(0,500, 500, 200))
                        renderGuess = font.render(guess, True, grey)
                        window.blit(renderGuess, (180, 530))
                        
                    else:
                        win = checkGuessLight(turns, word, guess, window)
                        turns+=1
                        guess = ""
                        #cc =window.fill(white,(0,500, 500, 200))
                

                        #window.fill(white,(0,500, 500, 200))
                ##colourblind
                # if event.key == K_LSHIFT:
                #     cbm = 1
                # if event.key == K_RETURN and cbm ==1 and len(guess) > 4:
                #     win = checkGuess2(turns, word, guess, window)
                #     turns+=1
                #     guess = ""
                #     window.fill(black,(0,500, 500, 200))
                

        ##chin colour 
        cc = window.fill(white,(0,500, 500, 200))
        renderGuess = font.render(guess, True, grey)
        window.blit(renderGuess, (180, 530))

        if win == True:
            window.fill(white)
            window.blit(youWin,(110,100))
            window.blit(bigFont.render("The word is", True, lred),(90,200))
            window.blit(bigFont.render(word[:-1], True, blue),(150,300))
            window.blit(playAgain,(90,400))
            
        ##printing word after losing
        #with backgrond removed
        if turns == 6 and win != True:
            window.fill(white)
            window.blit(youLose,(110,100))
            window.blit(bigFont.render("The word is", True, lred),(90,200))
            window.blit(bigFont.render(word[:-1], True, blue),(150,300))
            window.blit(playAgain,(90,400))
        pygame.display.update()
        clock.tick(FPS)
main()
