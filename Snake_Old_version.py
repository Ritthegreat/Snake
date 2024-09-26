##create display
##import graphics
##name the program
##set variables
import pygame
import random
import time
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((850,850))
pygame.display.set_caption('Snake')
black = ((0,0,0))
white = ((255,255,255))
blue = ((0,0,255))
red = ((255,0,0))
color = ((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
clock = pygame.time.Clock()
timer = 0
snakelist = [[200,300]]
foodx = 450
foody = 300
xchange=0
ychange=0
r = 0
l = 0

##Method to dislpay text on the screen
def show_text(msg,x,y,color):
    fontobj=pygame.font.SysFont("1",100)
    msgobj = fontobj.render(msg,False,color)
    screen.blit(msgobj,(x,y))

#Snakes method to play the game    
def snakes():    
    #adds delay in the game
    #declares lists and variables
    clock = pygame.time.Clock()
    snakelist = [[200,300]]
    timer = 0
    foodx = 450
    foody = 300
    xchange=0
    ychange=0
    r = 0
    l = 0
    t=10
    s= 10
    end=False

    while True:
        if end==True:
            end = False
            break

        ##adds delay between color change in text on the screen
        clock.tick(t)
        if timer%50==0:
            color = ((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        timer+=1

        ##constantly updates the display
        ##takes in arrow key input from the user on the direction of the snake
        pygame.display.update()
        screen.fill(white)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    ychange=-50
                    xchange=0
                if event.key == K_DOWN:
                    ychange = 50
                    xchange=0
                if event.key == K_RIGHT:
                    xchange = 50
                    ychange=0
                if event.key == K_LEFT:
                   xchange = -50
                   ychange=0

        ##makes the snake longer by increasing its length and adding it to a list
        ##draws the snake
        for y in range(0,750,50):
            for x in range(0,850,50):
                pygame.draw.rect(screen,black,(x,y,50,50),5)
        snakelist.insert(0,[snakelist[0][0]+xchange,snakelist[0][1]+ychange])
        snakelist.pop()

        ##determines if the snake collides with any of the walls by comparing
        ##the coordinates of the snake with the boundaries
        for snake in snakelist:
            pygame.draw.rect(screen,blue,(snake[0],snake[1],50,50))
            if snake[0] < -50:
                snake[0] = 0
                end = True
            if snake[0] > 850:
                snake[0] = 800
                end = True
            if snake[1] < 0:
                snake[1] = 0
                end = True
            if snake[1] > 700:
                snake[1] = 700
                end = True

        ##determines if the snake collides with itself
        pygame.draw.rect(screen,red,(foodx,foody,50,50))
        if [snakelist[0][0],snakelist[0][1]] in snakelist[1:]:
            end = True

        ##determines if the snake is in top of the food and adds length to the snake by increasing the list
        if snakelist[0][0] == foodx  and snakelist[0][1] == foody:
            foodx = random.randrange(0,850,50)
            foody = random.randrange(0,750,50)
            snakelist.append([snake[0],snake[1]])
            l = l + 1

        ##displays text on the screen
        show_text ("{}".format(l),650,750,color)
        show_text ('S',0,750,color)
        show_text ('N',100,750,color)
        show_text ('A',200,750,color)
        show_text ('K',300,750,color)
        show_text ('E',400,750,color)

    
##starting menu
def menu():
    screen.fill(black)
    play = False

    ##creates play and quit box and tracks mouse location
    while True:
        if play == True:
            break
        screen.fill(white)
        pygame.draw.rect(screen,color,(100,200,200,100),5)
        pygame.draw.rect(screen,color,(400,200,200,100),5)
        show_text ("Play",100,200,color)
        show_text ("Quit",400,200,color)

        #tracks mouse location on the text boxes
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x,y = event.pos
                if x in range (100,300) and y in range (200,300):
                    play = True
                if x in range (400,600) and y in range (200,300):
                    quit()
        pygame.display.update()

##introduces rules and asks user for confirmation to play the game
def introduceRules():
    print("Hello Welcome to Snake!!")
    print("")
    print("#RULES")
    print("You are the blue snake.")
    print("You can use the arrow keys on your keyboard to move the snake in any direction you want.")
    print("Your goal is to eat the food, the red square, and grow longer until your cover the entire board.")
    print("You must not run into yourself or run into the wall or else you lose.")
    print("Type yes to continue and no to quit")
    confirm = input()
    if confirm == "yes":
        while True:
            snakes()
            menu()
    elif confirm == "no":
        quit
    else:
        print ("invalid input try again")
        introduceRules()

#start of the whole program
introduceRules()


    
