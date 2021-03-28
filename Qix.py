from School.CPS406.Character import Character
from random import randint
from Graph import Graph

class Qix(Character):

    def __init__(self, cX, cY):
        self.moveD = 5
        Character.__init__( self, cX, cY, self.moveD)
        self.changeGrid = randint(1,20)
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

    def checkIntersection(self, g):
        options = []
        if self.coordXGrid < 99:
            if g.getGrid(self.coordXGrid+1, self.coordYGrid) == 0:
                options.append("RIGHT")
        if self.coordXGrid > 1:
            if g.getGrid(self.coordXGrid-1, self.coordYGrid) == 0:
                options.append("LEFT")
        if self.coordYGrid < 99:
            if g.getGrid(self.coordXGrid, self.coordYGrid+1) == 0:
                options.append("DOWN")
        if self.coordYGrid > 1:
            if g.getGrid(self.coordXGrid, self.coordYGrid-1) == 0:
                options.append("UP")
        return options

    def move(self, g):
        options = self.checkIntersection(g)
        if self.changeGrid == 0:
            self.direction = options[randint(0, len(options)-1)]
            self.changeGrid = randint(1,20)
        if self.direction == "UP":
            self.coordXP -= self.moveD
            self.changeGrid -=1
            if self.changeGrid:
                Character.moveUp()
                self.changeGrid = False
            else:
                self.changeGrid = True
        elif self.direction == "DOWN":
            self.coordXP += self.moveD
            self.changeGrid -=1
            if self.changeGrid:
                Character.moveDown()
                self.changeGrid = False
            else:
                self.changeGrid = True
        elif self.direction == "LEFT":
            self.coordYP -= self.moveD
            self.changeGrid -=1
            if self.changeGrid:
                Character.moveLeft()
                self.changeGrid = False
            else:
                self.changeGrid = True
        elif self.direction == "RIGHT":
            self.coordYP += self.moveD
            self.changeGrid -=1
            if self.changeGrid:
                Character.moveRight()
                self.changeGrid = False
            else:
                self.changeGrid = True
    
    def checkCollision(self, draw):
        if [self.coordXGrid, self.coordYGrid] in draw:
            return #have this do something