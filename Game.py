from Qix import Qix
import pygame
import time
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

    def writing(self):
        fontTitle = pygame.font.Font('freesansbold.ttf', 15)
        numTitle = pygame.font.Font('freesansbold.ttf', 20)
        lives = fontTitle.render('Lives', True, (225, 225, 225))
        currentP = fontTitle.render('Current %', True, (225, 225, 225))
        finalP = fontTitle.render('Final %', True, (225, 225, 225))
        numLives = numTitle.render(str(self.player.getLife()), True, (225, 225, 225))
        currentPNum = numTitle.render(str(round(self.backgroundGraph.getCurrentPercent()*100)) + "%", True, (225, 225, 225))
        finalPNum = numTitle.render("75%", True, (225, 225, 225))
        self.gameDisplay.blit(lives, (100, 20))
        self.gameDisplay.blit(currentP, (150, 20))
        self.gameDisplay.blit(finalP, (235, 20))
        self.gameDisplay.blit(numLives, (112, 43))
        self.gameDisplay.blit(currentPNum, (170, 43))
        self.gameDisplay.blit(finalPNum, (245, 43))
        return

    def drawImages(self):
        qixLogo = pygame.image.load('C:/Users/Theodore Wilson/Desktop/PYTHON/Ex_Files_Learning_Python/Exercise Files/School/CPS406/A2_attempt1/Images/qixLogo.JPG')
        self.gameDisplay.blit(qixLogo, (0, 20))

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
        self.writing()
        self.drawImages()#images at top
        self.pygameDrawLine() #lines
        pygame.draw.circle(self.gameDisplay, (0,128,0), [self.qix.getCoordYP(), self.qix.getCoordXP()],  2) #self.qix
        pygame.draw.circle(self.gameDisplay, (128,0,0), [self.player.getCoordYP(), self.player.getCoordXP()],  6) #self.player
        pygame.draw.circle(self.gameDisplay, (225,225,0), [self.spark1.getCoordYP(), self.spark1.getCoordXP()],  6) #self.spark1
        pygame.draw.circle(self.gameDisplay, (225,225,0), [self.spark2.getCoordYP(), self.spark2.getCoordXP()],  6) #self.spark2
        pygame.display.update()

    
    def play(self, c):
        self.backgroundGraph = Graph()
        self.backgroundGraph.setupGrid()
        self.player = Player(0,0)
        self.spark1 = Spark(69,69)
        self.spark2 = Spark(69,0)
        self.qix = Qix(35,35)
        Done = False

        self.pygameDraw()

        while (not Done):

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
                    return "Quit"

            #moves the self.player
            if spaceDown:
                if shiftDown:
                    if wDown:
                        if self.player.move(True, False, False, False, True, True, self.backgroundGraph, [self.qix.getCoordXGrid(), self.qix.getCoordYGrid()]):
                            return "Win"
                    elif aDown:
                        if self.player.move(False, False, True, False, True, True, self.backgroundGraph, [self.qix.getCoordXGrid(), self.qix.getCoordYGrid()]):
                            return "Win"
                    elif sDown:
                        if self.player.move(False, True, False, False, True, True, self.backgroundGraph, [self.qix.getCoordXGrid(), self.qix.getCoordYGrid()]):
                            return "Win"
                    elif dDown:
                        if self.player.move(False, False, False, True, True, True, self.backgroundGraph, [self.qix.getCoordXGrid(), self.qix.getCoordYGrid()]):
                            return "Win"
                else:
                    if wDown:
                        if self.player.move(True, False, False, False, True, False, self.backgroundGraph, [self.qix.getCoordXGrid(), self.qix.getCoordYGrid()]):
                            return "Win"
                    elif aDown:
                        if self.player.move(False, False, True, False, True, False, self.backgroundGraph, [self.qix.getCoordXGrid(), self.qix.getCoordYGrid()]):
                            return "Win"
                    elif sDown:
                        if self.player.move(False, True, False, False, True, False, self.backgroundGraph, [self.qix.getCoordXGrid(), self.qix.getCoordYGrid()]):
                            return "Win"
                    elif dDown:
                        if self.player.move(False, False, False, True, True, False, self.backgroundGraph, [self.qix.getCoordXGrid(), self.qix.getCoordYGrid()]):
                            return "Win"
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
                return "Lose"
            
            #moves the self.spark
            self.spark1.move(self.backgroundGraph, self.player)
            self.spark2.move(self.backgroundGraph, self.player)
            self.player.checkLoseLife(self.spark1.getCoordXGrid(), self.spark1.getCoordYGrid(), self.backgroundGraph)
            self.player.checkLoseLife(self.spark2.getCoordXGrid(), self.spark2.getCoordYGrid(), self.backgroundGraph)
            if self.player.getLife() == 0:
                return "Lose"


            #moves the self.qix
            self.qix.move(self.backgroundGraph, self.player)
            if self.player.getLife() == 0:
                return "Lose"
            self.pygameDraw()
            c.tick_busy_loop(30)

    def game(self):
        pygame.init()
        pygame.font.init()         
        
        self.gameDisplay = pygame.display.set_mode((300, 380))
        self.gameDisplay.fill((0,0,0))
        pygame.display.set_caption("Qix")
        clock = pygame.time.Clock()#sets Fps
        isDone = False

        #self.pygameDraw()

        while not isDone:

            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    isDone = True
            
            home = self.homeScreen()
            if home == "Game":
                game = self.play(clock)
                if game == "Win":
                    self.winScreen()
                elif game == "Lose":
                    self.loseScreen()
                elif game == "Quit":
                    isDone = True
                    break
            elif home == "Controls":
                controls = self.instructionScreen()
                if controls == "Quit":
                    isDone = True
                    break
            elif home == "Quit":
                isDone = True
                break


            clock.tick_busy_loop(30)

        #Ends Pygame
        pygame.quit()
        quit()
    
    def winScreen(self):
        self.gameDisplay.fill((0,0,0))
        font = pygame.font.Font('freesansbold.ttf', 50)
        you = font.render('YOU', True, (225, 225, 225))
        win = font.render('WIN!', True, (225, 225, 225))
        self.gameDisplay.blit(you, (95, 140))
        self.gameDisplay.blit(win, (95, 190))
        pygame.display.update()
        pygame.time.delay(10000)

    def loseScreen(self):
        self.gameDisplay.fill((0,0,0))
        font = pygame.font.Font('freesansbold.ttf', 50)
        you = font.render('YOU', True, (225, 225, 225))
        win = font.render('LOSE', True, (225, 225, 225))
        self.gameDisplay.blit(you, (95, 140))
        self.gameDisplay.blit(win, (82, 190))
        pygame.display.update()
        pygame.time.delay(10000)

    def homeScreen(self):
        Done = False
        while (not Done):
            self.gameDisplay.fill((0,0,0))

            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    return "Quit"

            if pygame.mouse.get_pressed()[0] == 1:
                mouse = pygame.mouse.get_pos()
                if mouse[1] > 150 and mouse[1] < 180 and mouse[0] > 75 and mouse[0] < 225:
                    return "Game"

            if pygame.mouse.get_pressed()[0] == 1:
                mouse = pygame.mouse.get_pos()
                if mouse[1] > 210 and mouse[1] < 240 and mouse[0] > 75 and mouse[0] < 225:
                    return "Controls"
            
            if pygame.mouse.get_pressed()[0] == 1:
                mouse = pygame.mouse.get_pos()
                if mouse[1] > 270 and mouse[1] < 300 and mouse[0] > 75 and mouse[0] < 225:
                    return "Quit"

            qixLogo = pygame.image.load('C:/Users/Theodore Wilson/Desktop/PYTHON/Ex_Files_Learning_Python/Exercise Files/School/CPS406/A2_attempt1/Images/qixLogo.JPG')
            qixRect = qixLogo.get_rect()
            qixRect.center = (150, 80)
            self.gameDisplay.blit(qixLogo, qixRect)

            button = pygame.font.Font(None, 40)

            game = button.render('Play', True, (0,0,0))
            gameRect = game.get_rect()
            gameRect.center = (150, 165)
            pygame.draw.rect(self.gameDisplay, (225,225,225), [75, 150, 150, 30])
            self.gameDisplay.blit(game, gameRect)

            c = button.render('Controls', True, (0,0,0))
            cRect = c.get_rect()
            cRect.center = (150, 225)
            pygame.draw.rect(self.gameDisplay, (225,225,225), [75, 210, 150, 30])
            self.gameDisplay.blit(c, cRect)

            q = button.render('Quit', True, (0,0,0))
            qRect = q.get_rect()
            qRect.center = (150, 285)
            pygame.draw.rect(self.gameDisplay, (225,225,225), [75, 270, 150, 30])
            self.gameDisplay.blit(q, qRect)

            pygame.display.update()
    
    def instructionScreen(self):
        Done = False
        while (not Done):
            self.gameDisplay.fill((0,0,0))

            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    return "Quit"

            if pygame.mouse.get_pressed()[0] == 1:
                mouse = pygame.mouse.get_pos()
                if mouse[1] > 0 and mouse[1] < 30 and mouse[0] > 0 and mouse[0] < 60:
                    return "Back"

            button = pygame.font.Font(None, 30)
            title = pygame.font.Font('freesansbold.ttf', 32)
            key = pygame.font.Font('freesansbold.ttf', 25)
            intstrct = title.render('Controls', True, (225, 225, 225))

            w = key.render('W = Go up', True, (225, 225, 225))
            a = key.render('A = Go left', True, (225, 225, 225))
            s = key.render('S = Go down', True, (225, 225, 225))
            d = key.render('D = Go right', True, (225, 225, 225))
            space = key.render('SPACE = Draw', True, (225, 225, 225))
            shSpace = key.render('SHIFT = Slow Speed', True, (225, 225, 225))
            back = button.render('Back', True, (0,0,0))

            iRect = intstrct.get_rect()
            iRect.center = (150, 25)
            wRect = w.get_rect()
            wRect.center = (150, 70)
            aRect = a.get_rect()
            aRect.center = (150, 115)
            sRect = s.get_rect()
            sRect.center = (150, 160)
            dRect = d.get_rect()
            dRect.center = (150, 205)
            spaceRect = space.get_rect()
            spaceRect.center = (150, 250)
            shRect = shSpace.get_rect()
            shRect.center = (150, 295)
            bRect = back.get_rect()
            bRect.center = (30, 15)

            pygame.draw.rect(self.gameDisplay, (225, 225, 225), [0, 30, 60, -30])
            self.gameDisplay.blit(intstrct, iRect)
            self.gameDisplay.blit(w, wRect)
            self.gameDisplay.blit(a, aRect)
            self.gameDisplay.blit(s, sRect)
            self.gameDisplay.blit(d, dRect)
            self.gameDisplay.blit(space, spaceRect)
            self.gameDisplay.blit(shSpace, shRect)
            self.gameDisplay.blit(back, bRect)

            pygame.display.update()