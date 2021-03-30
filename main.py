from Qix import Qix
import pygame
from Player import Player
from Graph import Graph
from Spark import Spark

def pygameDrawLine():
    for i in range(101):
        for j in range(101):
            if backgroundGraph.getDirectionGrid(i, j) == "VU":
                pygame.draw.line(gameDisplay, (0,0,0,), [j*10+5, i*10+5], [j*10+5, i*10+15], 3)
                #pygame.draw.rect(gameDisplay, (0,0,0,), [j*10+5, i*10+5, 3, -10])
            if backgroundGraph.getDirectionGrid(i, j) == "VD":
                pygame.draw.line(gameDisplay, (0,0,0,), [j*10+5, i*10-5], [j*10+5, i*10+5], 3)
                #pygame.draw.rect(gameDisplay, (0,0,0,), [j*10+5, i*10-5, 3, 10])
            elif backgroundGraph.getDirectionGrid(i, j) == "HL":
                pygame.draw.line(gameDisplay, (0,0,0,), [j*10+5, i*10+5], [j*10+10+5, i*10+5], 3)
                #pygame.draw.rect(gameDisplay, (0,0,0,), [j*10+5, i*10+5, -10, 3])
            elif backgroundGraph.getDirectionGrid(i, j) == "HR":
                pygame.draw.line(gameDisplay, (0,0,0,), [j*10-5, i*10+5], [j*10+5, i*10+5], 3)
                #pygame.draw.rect(gameDisplay, (0,0,0,), [j*10-5, i*10+5, 10, 3])

def pygameDraw():
    pygame.draw.rect(gameDisplay, (0,0,0), [0, 0, 1010, 1010]) #black background
    pygame.draw.rect(gameDisplay, (0,128,0), [5, 5, 1000, 1000]) #play area
    pygameDrawLine() #lines
    pygame.draw.circle(gameDisplay, (0,0,0), [qix.getCoordYP(), qix.getCoordXP()],  5) #qix
    pygame.draw.circle(gameDisplay, (128,0,0), [player.getCoordYP(), player.getCoordXP()],  5) #player
    pygame.draw.circle(gameDisplay, (0,0,128), [spark1.getCoordYP(), spark1.getCoordXP()],  5) #spark
    if numSparks == 2:
        None
    pygame.display.update()

numSparks = 1
backgroundGraph = Graph()
backgroundGraph.setupGrid()
backgroundGraph.setupDirectionGrid()
player = Player(0,0)
spark1 = Spark(0,50)
qix = Qix(50,50)

pygame.init()    

gameDisplay = pygame.display.set_mode((1010, 1010))
pygame.display.set_caption("Qix")
clock = pygame.time.Clock()#sets Fps
isDone = False

pygameDraw()

while not isDone:

    pressed = pygame.key.get_pressed()

    spaceDown = pressed[pygame.K_SPACE]
    wDown = pressed[pygame.K_w]
    aDown = pressed[pygame.K_a]
    sDown = pressed[pygame.K_s]
    dDown = pressed[pygame.K_d]

    for event in pygame.event.get(): #checks for what is happening in the game
        #Checks if X is clicked. If is quits Pygame
        if event.type == pygame.QUIT:
            isDone = True

    #moves the player
    if spaceDown:
        if wDown:
            player.move(True, False, False, False, True, backgroundGraph)
        elif aDown:
            player.move(False, False, True, False, True, backgroundGraph)
        elif sDown:
            player.move(False, True, False, False, True, backgroundGraph)
        elif dDown:
            player.move(False, False, False, True, True, backgroundGraph)
    else:
        if wDown:
            player.move(True, False, False, False, False, backgroundGraph)
        elif aDown:
            player.move(False, False, True, False, False, backgroundGraph)
        elif sDown:
            player.move(False, True, False, False, False, backgroundGraph)
        elif dDown:
            player.move(False, False, False, True, False, backgroundGraph)
    pygameDraw()
    

    #moves the spark
    spark1.move(backgroundGraph)
    pygameDraw()
    if numSparks == 2:
        None #when i add the ability to create a second spark
    player.checkLoseLife(spark1.getCoordXGrid(), spark1.getCoordYGrid())
    pygameDraw()


    #moves the qix
    qix.move(backgroundGraph, player)
    pygameDraw()


    pygame.display.update()
    clock.tick(60)

#Ends Pygame
pygame.quit()
quit()