from Character import Character
from random import randint
from Graph import Graph

class Qix(Character):

    def __init__(self, cX, cY):
        self.moveD = 5
        Character.__init__( self, cX, cY, cX*10+5, cY*10+5, self.moveD)
        self.changeGrid = False
        self.changeD = randint(20,80)
        #print (self.changeGrid)
        self.direction = self.randDirection(4)
    
    def randDirection(self, max):
        rand = randint(1,max)
        if rand == 1:
            return "UP"
        if rand == 2:
            return "DOWN"
        if rand == 3:
            return "LEFT"
        if rand == 4:
            return "RIGHT"

    def checkWall(self, g, p):
        if self.coordYGrid < 100:
            if g.getGrid(self.coordXGrid, self.coordYGrid+1) == 1:
                if [self.coordXGrid, self.coordYGrid+1] in p.getDraw():
                    self.checkCollision(self.coordXGrid, self.coordYGrid+1, p, g)
                return True
        if self.coordYGrid > 0:
            if g.getGrid(self.coordXGrid, self.coordYGrid-1) == 1:
                if [self.coordXGrid, self.coordYGrid-1] in p.getDraw():
                    self.checkCollision(self.coordXGrid, self.coordYGrid-1, p, g)
                return True
        if self.coordXGrid < 100:
            if g.getGrid(self.coordXGrid+1, self.coordYGrid) == 1:
                if [self.coordXGrid+1, self.coordYGrid] in p.getDraw():
                    self.checkCollision(self.coordXGrid+1, self.coordYGrid, p, g)
                return True
        if self.coordXGrid > 0:
            if g.getGrid(self.coordXGrid-1, self.coordYGrid) == 1:
                if [self.coordXGrid-1, self.coordYGrid] in p.getDraw():
                    self.checkCollision(self.coordXGrid-1, self.coordYGrid, p, g)
                return True
        return False

    def checkIntersection(self, g):
        options = []
        if self.coordYGrid < 100:
            if g.getGrid(self.coordXGrid, self.coordYGrid+1) == 0:
                options.append("RIGHT")
        if self.coordYGrid > 0:
            if g.getGrid(self.coordXGrid, self.coordYGrid-1) == 0:
                options.append("LEFT")
        if self.coordXGrid < 100:
            if g.getGrid(self.coordXGrid+1, self.coordYGrid) == 0:
                options.append("DOWN")
        if self.coordXGrid > 0:
            if g.getGrid(self.coordXGrid-1, self.coordYGrid) == 0:
                options.append("UP")
        return options

    def move(self, g, p):
        #print (self.changeGrid)
        #print (self.coordXGrid)
        #print (self.coordYGrid)
        #print ()
        options = self.checkIntersection(g)
        if self.checkWall(g, p):
            #print ("1")
            self.changeD = 0
        if self.changeD == 0:
            #print ("2")
            self.direction = options[randint(0, len(options)-1)]
            self.changeD = randint(20,60)
        if self.direction == "UP":
            self.coordXP -= self.moveD
            self.changeD -=1
            if self.changeGrid:
                Character.moveUp(self)
                self.changeGrid = False
            else:
                self.changeGrid = True
        elif self.direction == "DOWN":
            self.coordXP += self.moveD
            self.changeD -=1
            if self.changeGrid:
                Character.moveDown(self)
                self.changeGrid = False
            else:
                self.changeGrid = True
        elif self.direction == "LEFT":
            self.coordYP -= self.moveD
            self.changeD -=1
            if self.changeGrid:
                Character.moveLeft(self)
                self.changeGrid = False
            else:
                self.changeGrid = True
        elif self.direction == "RIGHT":
            self.coordYP += self.moveD
            self.changeD -=1
            if self.changeGrid:
                Character.moveRight(self)
                self.changeGrid = False
            else:
                self.changeGrid = True
    
    def checkCollision(self, draw, p, g):
        print ("a")
        p.qixHit(g)