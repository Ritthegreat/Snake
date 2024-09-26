import pygame
import random
import time
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('Snake')
black = ((0,0,0))
white = ((255,255,255))
green = ((0,128,0))
yellow = ((255,255,0))                              
aqua = ((0,255,255))
blue = ((0,0,255))
red = ((255,0,0))
color = ((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
foodx = 450
foody = 300
s = 300
a = 300
x = 200
y = 300
keyup =0
keydown =0 
keyleft =0
keyright=0
ychange = 0
xchange = 50
w = 50
xs = 0
ys = 0
backsound = pygame.mixer.Sound('battleThemeA.wav')
clock = pygame.time.Clock()
def show_text(msg,x,y,color):
    fontobj=pygame.font.SysFont("1",100)
    msgobj = fontobj.render(msg,False,color)
    screen.blit(msgobj,(x,y))
timer = 0
while True:
    print(x,y)

    clock.tick(5)
    if timer%50==0:
        color = ((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    timer+=1
    backsound.play()
    pygame.display.update()
    screen.fill(black)
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
    y = y + ychange
    x = x + xchange 
    pygame.draw.line(screen,color,(50,0),(50,600),5)
    pygame.draw.line(screen,color,(100,0),(100,600),5)
    pygame.draw.line(screen,color,(150,0),(150,600),5)
    pygame.draw.line(screen,color,(200,0),(200,600),5)
    pygame.draw.line(screen,color,(250,0),(250,600),5)
    pygame.draw.line(screen,color,(300,0),(300,600),5)
    pygame.draw.line(screen,color,(350,0),(350,600),5)
    pygame.draw.line(screen,color,(400,0),(400,600),5)
    pygame.draw.line(screen,color,(450,0),(450,600),5)
    pygame.draw.line(screen,color,(500,0),(500,600),5)
    pygame.draw.line(screen,color,(550,0),(550,600),5)
    pygame.draw.line(screen,color,(0,50),(600,50),5)
    pygame.draw.line(screen,color,(0,100),(600,100),5)
    pygame.draw.line(screen,color,(0,150),(600,150),5)
    pygame.draw.line(screen,color,(0,200),(600,200),5)
    pygame.draw.line(screen,color,(0,250),(600,250),5)
    pygame.draw.line(screen,color,(0,300),(600,300),5)
    pygame.draw.line(screen,color,(0,350),(600,350),5)
    pygame.draw.line(screen,color,(0,400),(600,400),5)
    pygame.draw.line(screen,color,(0,450),(600,450),5)
    pygame.draw.line(screen,color,(0,500),(600,500),5)
    pygame.draw.line(screen,color,(0,550),(600,550),5)
    pygame.draw.rect(screen,red,(foodx,foody,50,50))
    pygame.draw.rect(screen,blue,(x,y,100,50))
    if x == foodx  and y == foody:
        foodx = random.randrange(0,600,50)
        foody = random.randrange(0,600,50)       
    if x <= 0:
        print ('gameover')
    if x >= 600:
        print ('gameover')
    if y <= 50:
        y = 50
        print ('gameover')
    if y >= 600:
        y = 500
        print ('gameover')

    
 
    
    
