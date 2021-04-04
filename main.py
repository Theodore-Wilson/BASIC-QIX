from Qix import Qix
import pygame
from Player import Player
from Graph import Graph
from Spark import Spark



def pygameDrawLine():
    for i in range(70):
        for j in range(70):
            if backgroundGraph.getGrid(i, j) >= 1:
                if backgroundGraph.getCGrid(i,j) == "w":
                    pygame.draw.rect(gameDisplay, (225,225,225), [easyCalcX[j], easyCalcY[i], 4, 4])
                elif backgroundGraph.getCGrid(i,j) == "b":
                    pygame.draw.rect(gameDisplay, (0,0,225), [easyCalcX[j], easyCalcY[i], 4, 4])
                elif backgroundGraph.getCGrid(i,j) == "r":
                    pygame.draw.rect(gameDisplay, (225,100,100), [easyCalcX[j], easyCalcY[i], 4, 4])

def pygameDraw():
    gameDisplay.fill((0,0,0))
    pygameDrawLine() #lines
    pygame.draw.circle(gameDisplay, (0,128,0), [qix.getCoordYP(), qix.getCoordXP()],  2) #qix
    pygame.draw.circle(gameDisplay, (128,0,0), [player.getCoordYP(), player.getCoordXP()],  6) #player
    pygame.draw.circle(gameDisplay, (225,225,0), [spark1.getCoordYP(), spark1.getCoordXP()],  6) #spark1
    pygame.draw.circle(gameDisplay, (225,225,0), [spark2.getCoordYP(), spark2.getCoordXP()],  6) #spark2
    pygame.display.update()

backgroundGraph = Graph()
backgroundGraph.setupGrid()
player = Player(0,0)
spark1 = Spark(69,69)
spark2 = Spark(69,0)
qix = Qix(35,35)
easyCalcX = [(i * 4 +10) for i in range(70)]
easyCalcY = [(i * 4 +90) for i in range(70)]

pygame.init()         

gameDisplay = pygame.display.set_mode((300, 380))
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
                if player.move(True, False, False, False, True, True, backgroundGraph, [qix.getCoordXGrid(), qix.getCoordYGrid()]):
                    isDone = True
            elif aDown:
                if player.move(False, False, True, False, True, True, backgroundGraph, [qix.getCoordXGrid(), qix.getCoordYGrid()]):
                    isDone = True
            elif sDown:
                if player.move(False, True, False, False, True, True, backgroundGraph, [qix.getCoordXGrid(), qix.getCoordYGrid()]):
                    isDone = True
            elif dDown:
                if player.move(False, False, False, True, True, True, backgroundGraph, [qix.getCoordXGrid(), qix.getCoordYGrid()]):
                    isDone = True
        else:
            if wDown:
                if player.move(True, False, False, False, True, False, backgroundGraph, [qix.getCoordXGrid(), qix.getCoordYGrid()]):
                    isDone = True
            elif aDown:
                if player.move(False, False, True, False, True, False, backgroundGraph, [qix.getCoordXGrid(), qix.getCoordYGrid()]):
                    isDone = True
            elif sDown:
                if player.move(False, True, False, False, True, False, backgroundGraph, [qix.getCoordXGrid(), qix.getCoordYGrid()]):
                    isDone = True
            elif dDown:
                if player.move(False, False, False, True, True, False, backgroundGraph, [qix.getCoordXGrid(), qix.getCoordYGrid()]):
                    isDone = True
    else:
        if wDown:
            player.move(True, False, False, False, False, False, backgroundGraph, [qix.getCoordXGrid(), qix.getCoordYGrid()])
        elif aDown:
            player.move(False, False, True, False, False, False, backgroundGraph, [qix.getCoordXGrid(), qix.getCoordYGrid()])
        elif sDown:
            player.move(False, True, False, False, False, False, backgroundGraph, [qix.getCoordXGrid(), qix.getCoordYGrid()])
        elif dDown:
            player.move(False, False, False, True, False, False, backgroundGraph, [qix.getCoordXGrid(), qix.getCoordYGrid()])
    if player.getLife() == 0:    
        isDone = True
    
    #moves the spark
    spark1.move(backgroundGraph, player)
    spark2.move(backgroundGraph, player)
    player.checkLoseLife(spark1.getCoordXGrid(), spark1.getCoordYGrid(), backgroundGraph)
    player.checkLoseLife(spark2.getCoordXGrid(), spark2.getCoordYGrid(), backgroundGraph)
    if player.getLife() == 0:
        isDone = True


    #moves the qix
    qix.move(backgroundGraph, player)
    if player.getLife() == 0:
        isDone = True
    pygameDraw()
    clock.tick_busy_loop(30)

#Ends Pygame
pygame.quit()
quit()