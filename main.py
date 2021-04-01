from Qix import Qix
import pygame
from Player import Player
from Graph import Graph
from Spark import Spark

def pygameDrawLine():
    for i in range(100):
        for j in range(100):
            if backgroundGraph.getGrid(i, j) == 1:
                if backgroundGraph.getCGrid(i,j) == "w":
                    pygame.draw.rect(gameDisplay, (225,225,225), [j*4+10, i*4 + 90, 4, 4])
                elif backgroundGraph.getCGrid(i,j) == "b":
                    pygame.draw.rect(gameDisplay, (0,0,225), [j*4+10, i*4 + 90, 4, 4])
                elif backgroundGraph.getCGrid(i,j) == "r":
                    pygame.draw.rect(gameDisplay, (225,100,100), [j*4+10, i*4 + 90, 4, 4])

def pygameDraw():
    gameDisplay.fill((0,0,0))
    pygameDrawLine() #lines
    pygame.draw.circle(gameDisplay, (0,128,0), [qix.getCoordYP(), qix.getCoordXP()],  6) #qix
    pygame.draw.circle(gameDisplay, (128,0,0), [player.getCoordYP(), player.getCoordXP()],  6) #player
    pygame.draw.circle(gameDisplay, (225,225,0), [spark1.getCoordYP(), spark1.getCoordXP()],  6) #spark
    if numSparks == 2:
        None
    pygame.display.update()

numSparks = 1
backgroundGraph = Graph()
backgroundGraph.setupGrid()
player = Player(0,0)
spark1 = Spark(99,99)
qix = Qix(50,50)

pygame.init()    

gameDisplay = pygame.display.set_mode((420, 500))
gameDisplay.fill((0,0,0))
pygame.display.set_caption("Qix")
clock = pygame.time.Clock()#sets Fps
isDone = False

pygameDraw()

while not isDone:

    pressed = pygame.key.get_pressed()

    spaceDown = pressed[pygame.K_SPACE]
    shiftDown = pressed[pygame.K_LSHIFT]
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
        if shiftDown:
            if wDown:
                player.move(True, False, False, False, True, True, backgroundGraph)
            elif aDown:
                player.move(False, False, True, False, True, True, backgroundGraph)
            elif sDown:
                player.move(False, True, False, False, True, True, backgroundGraph)
            elif dDown:
                player.move(False, False, False, True, True, True, backgroundGraph)
        else:
            if wDown:
                player.move(True, False, False, False, True, False, backgroundGraph)
            elif aDown:
                player.move(False, False, True, False, True, False, backgroundGraph)
            elif sDown:
                player.move(False, True, False, False, True, False, backgroundGraph)
            elif dDown:
                player.move(False, False, False, True, True, False, backgroundGraph) 
    else:
        if wDown:
            player.move(True, False, False, False, False, False, backgroundGraph)
        elif aDown:
            player.move(False, False, True, False, False, False, backgroundGraph)
        elif sDown:
            player.move(False, True, False, False, False, False, backgroundGraph)
        elif dDown:
            player.move(False, False, False, True, False, False, backgroundGraph)
    pygameDraw()
    
    #moves the spark
    spark1.move(backgroundGraph)
    pygameDraw()
    if numSparks == 2:
        None #when i add the ability to create a second spark
    player.checkLoseLife(spark1.getCoordXGrid(), spark1.getCoordYGrid())
    pygameDraw()


    '''#moves the qix
    qix.move(backgroundGraph, player)
    pygameDraw()'''


    pygame.display.update()
    clock.tick(60)

#Ends Pygame
pygame.quit()
quit()