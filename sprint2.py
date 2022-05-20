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
##purpe for testing
purple = (127,0,255)

##actual font for original wordle is Neue Helvetica 75 Bold
font = pygame.font.SysFont("Helvetica neue bold", 55)
bigFont = pygame.font.SysFont("Helvetica neue bold", 80)

youWin = bigFont.render("Well Done!", True, green)
youLose = bigFont.render("Nice Try!", True, lred)
playAgain = bigFont.render("Play Again?", True, lgrey)

##global tile variables
a = lgrey
b = yellow
c = green
##assigns variable for colour blind greys
cbgrey = lgrey
##frame colour, light grey 2 by default
frame = lgrey2

##check guess universal attempt
def checkGuess(turns, word, userGuess, window):
    
    renderList = ["","","","",""]
    spacing = 0
    guessColourCode = [a,a,a,a,a]

    for x in range(0,5):
        if userGuess[x] in word:
            guessColourCode[x] = b

        if word[x] == userGuess[x]:
            guessColourCode[x] = c

    list(userGuess)

    for x in range(0,5):
        renderList[x] = font.render(userGuess[x], True, white)
        ##frames (50+(x*76), 50+(y*76), 70, 70),2)
        pygame.draw.rect(window, guessColourCode[x], pygame.Rect(50 +spacing, 50+ (turns*76), 70, 70))
        window.blit(renderList[x], (70 + spacing, 70 + (turns*76)))
        spacing+=76

    if guessColourCode == [c,c,c,c,c]:
        return True

##dark mode
def checkGuessDark(turns, word, userGuess, window):
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


def main():
    file = open("wordList.txt","r")
    wordList = file.readlines()
    word = wordList[random.randint(0, len(wordList)-1)].upper()

    ##background colour
    bg = white

    height = 600
    width = 500

    FPS = 30
    clock = pygame.time.Clock()

    window = pygame.display.set_mode((width, height))
    ##background colopur default white
    window.fill(bg)

    guess = ""

    print(word)

    for x in range(0,5):
        for y in range(0,6):
            pygame.draw.rect(window, lgrey2, pygame.Rect(50+(x*76), 50+(y*76), 70, 70),2)

    pygame.display.set_caption("Wordle")

    turns = 0
    win = False

    ##chin starting with white
    chinny = white

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

               
                ##
                if event.key == K_RETURN and len(guess) > 4:
                    k = pygame.key.get_pressed()
                    ##holding L shsift and type soemthing then enter to enter dark mode
                    ##then you no longer need to hold l shift
                    ##dark mode L shift
                    if k[pygame.K_LSHIFT]:
                        ##global variables
                        global a 
                        global b
                        global c
                        global cbgrey
                        global frame
                        a = grey
                        b = yellow
                        c = green
                        frame = grey
                        win = checkGuess(turns, word, guess, window)
                        window.fill(black)
                        #
                        turns+=1
                        guess = ""
                        #window.fill(white,(0,500, 500, 200))
                        guess = ""

                        print(word)

                        for x in range(0,5):
                            for y in range(0,6):
                                pygame.draw.rect(window, frame, pygame.Rect(50+(x*76), 50+(y*76), 70, 70),2)

                        pygame.display.set_caption("Wordle")

                        turns = 0
                        win = False
                        chinny = black
                        ##changes win-screen background to dark mode
                        bg = black
                        ##making cbgrey dark grey
                        cbgrey = grey
                        
                    ## cb mode- holding R-shift, after first word doesnt need to be held anymore
                    ##works in both light and dark modes,
                    elif k[pygame.K_RSHIFT] and event.key == K_RETURN: 
                        
                        a = cbgrey
                        b = blue
                        c = orange  
                        win = checkGuess(turns, word, guess, window)
                        turns+=1
                        guess = ""
                        window.fill(black,(0,500, 500, 200))

                    ##default light mode
                    else:
                        win = checkGuess(turns, word, guess, window)
                        turns+=1
                        guess = ""
                        
                

        ##chin assigbnment
        cc = window.fill(chinny,(0,500, 500, 200))
        renderGuess = font.render(guess, True, grey)
        window.blit(renderGuess, (180, 530))

        if win == True:
            window.fill(bg)
            window.blit(youWin,(110,100))
            window.blit(bigFont.render("The word is", True, lgrey),(90,200))
            window.blit(bigFont.render(f'"{word[:-1]}"', True, blue),(120,300))
            window.blit(playAgain,(90,400))
            
        ##printing word after losing
        #with backgrond removed
        if turns == 6 and win != True:
            window.fill(bg)
            window.blit(youLose,(130,100))
            window.blit(bigFont.render("The word is", True, lgrey),(90,200))
            window.blit(bigFont.render(f'"{word[:-1]}"', True, blue),(120,300))
            window.blit(playAgain,(90,400))
        pygame.display.update()
        clock.tick(FPS)
main()
