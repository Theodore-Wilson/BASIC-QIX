from Qix import Qix
import pygame
from Player import Player
from Graph import Graph
from Spark import Spark


class Game():

    def __init__(self):
        self.backgroundGraph = Graph()
        self.backgroundGraph.setupGrid()
        self.player = Player(0,0)
        self.spark1 = Spark(69,69)
        self.spark2 = Spark(69,0)
        self.qix = Qix(35,35)
        self.easyCalcX = [(i * 4 +10) for i in range(70)]
        self.easyCalcY = [(i * 4 +90) for i in range(70)]

    def pygameDrawLine(self):
        for i in range(70):
            for j in range(70):
                if self.backgroundGraph.getGrid(i, j) >= 1:
                    if self.backgroundGraph.getCGrid(i,j) == "w":
                        pygame.draw.rect(self.gameDisplay, (225,225,225), [self.easyCalcX[j], self.easyCalcY[i], 4, 4])
                    elif self.backgroundGraph.getCGrid(i,j) == "b":
                        pygame.draw.rect(self.gameDisplay, (0,0,225), [self.easyCalcX[j], self.easyCalcY[i], 4, 4])
                    elif self.backgroundGraph.getCGrid(i,j) == "r":
                        pygame.draw.rect(self.gameDisplay, (225,100,100), [self.easyCalcX[j], self.easyCalcY[i], 4, 4])

    def pygameDraw(self):
        self.gameDisplay.fill((0,0,0))
        self.pygameDrawLine() #lines
        pygame.draw.circle(self.gameDisplay, (0,128,0), [self.qix.getCoordYP(), self.qix.getCoordXP()],  2) #self.qix
        pygame.draw.circle(self.gameDisplay, (128,0,0), [self.player.getCoordYP(), self.player.getCoordXP()],  6) #self.player
        pygame.draw.circle(self.gameDisplay, (225,225,0), [self.spark1.getCoordYP(), self.spark1.getCoordXP()],  6) #self.spark1
        pygame.draw.circle(self.gameDisplay, (225,225,0), [self.spark2.getCoordYP(), self.spark2.getCoordXP()],  6) #self.spark2
        pygame.display.update()

    
    def game(self):
        pygame.init()         

        self.gameDisplay = pygame.display.set_mode((300, 380))
        self.gameDisplay.fill((0,0,0))
        pygame.display.set_caption("Qix")
        clock = pygame.time.Clock()#sets Fps
        isDone = False

        self.pygameDraw()

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

            #moves the self.player
            if spaceDown:
                if shiftDown:
                    if wDown:
                        if self.player.move(True, False, False, False, True, True, self.backgroundGraph, [self.qix.getCoordXGrid(), self.qix.getCoordYGrid()]):
                            isDone = True
                    elif aDown:
                        if self.player.move(False, False, True, False, True, True, self.backgroundGraph, [self.qix.getCoordXGrid(), self.qix.getCoordYGrid()]):
                            isDone = True
                    elif sDown:
                        if self.player.move(False, True, False, False, True, True, self.backgroundGraph, [self.qix.getCoordXGrid(), self.qix.getCoordYGrid()]):
                            isDone = True
                    elif dDown:
                        if self.player.move(False, False, False, True, True, True, self.backgroundGraph, [self.qix.getCoordXGrid(), self.qix.getCoordYGrid()]):
                            isDone = True
                else:
                    if wDown:
                        if self.player.move(True, False, False, False, True, False, self.backgroundGraph, [self.qix.getCoordXGrid(), self.qix.getCoordYGrid()]):
                            isDone = True
                    elif aDown:
                        if self.player.move(False, False, True, False, True, False, self.backgroundGraph, [self.qix.getCoordXGrid(), self.qix.getCoordYGrid()]):
                            isDone = True
                    elif sDown:
                        if self.player.move(False, True, False, False, True, False, self.backgroundGraph, [self.qix.getCoordXGrid(), self.qix.getCoordYGrid()]):
                            isDone = True
                    elif dDown:
                        if self.player.move(False, False, False, True, True, False, self.backgroundGraph, [self.qix.getCoordXGrid(), self.qix.getCoordYGrid()]):
                            isDone = True
            else:
                if wDown:
                    self.player.move(True, False, False, False, False, False, self.backgroundGraph, [self.qix.getCoordXGrid(), self.qix.getCoordYGrid()])
                elif aDown:
                    self.player.move(False, False, True, False, False, False, self.backgroundGraph, [self.qix.getCoordXGrid(), self.qix.getCoordYGrid()])
                elif sDown:
                    self.player.move(False, True, False, False, False, False, self.backgroundGraph, [self.qix.getCoordXGrid(), self.qix.getCoordYGrid()])
                elif dDown:
                    self.player.move(False, False, False, True, False, False, self.backgroundGraph, [self.qix.getCoordXGrid(), self.qix.getCoordYGrid()])
            if self.player.getLife() == 0:    
                isDone = True
            
            #moves the self.spark
            self.spark1.move(self.backgroundGraph, self.player)
            self.spark2.move(self.backgroundGraph, self.player)
            self.player.checkLoseLife(self.spark1.getCoordXGrid(), self.spark1.getCoordYGrid(), self.backgroundGraph)
            self.player.checkLoseLife(self.spark2.getCoordXGrid(), self.spark2.getCoordYGrid(), self.backgroundGraph)
            if self.player.getLife() == 0:
                isDone = True


            #moves the self.qix
            self.qix.move(self.backgroundGraph, self.player)
            if self.player.getLife() == 0:
                isDone = True
            self.pygameDraw()
            clock.tick_busy_loop(30)

        #Ends Pygame
        pygame.quit()
        quit()