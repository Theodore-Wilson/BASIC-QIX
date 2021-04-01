from Character import Character
from random import randint
from Graph import Graph

class Spark(Character):

    def __init__(self, cX, cY):
        self.moveD = 2
        Character.__init__( self, cX, cY, cX*4+92, cY*4+10, self.moveD)
        self.changeGrid = False
        self.direction = "RIGHT"

    def checkIntersection(self, g):
        options = []
        if self.coordYGrid < 99:
            if g.getGrid(self.coordXGrid, self.coordYGrid+1) == 1:
                options.append("RIGHT")
        if self.coordYGrid > 0:
            if g.getGrid(self.coordXGrid, self.coordYGrid-1) == 1:
                options.append("LEFT")
        if self.coordXGrid < 99:
            if g.getGrid(self.coordXGrid+1, self.coordYGrid) == 1:
                options.append("DOWN")
        if self.coordXGrid > 0:
            if g.getGrid(self.coordXGrid-1, self.coordYGrid) == 1:
                options.append("UP")
        return options

    def move(self, g):
        if self.changeGrid:
            options = self.checkIntersection(g)
            if not(len(options) == 2 and (("UP" in options and "DOWN" in options) or ("LEFT" in options and "RIGHT" in options))):
                if len(options) > 0:
                    rand = randint(0,len(options)-1)
                    self.direction = options[rand]
        if self.direction == "UP":
            self.coordXP -= self.moveD
            if self.changeGrid:
                Character.moveUp(self)
                self.changeGrid = False
            else:
                self.changeGrid = True
        elif self.direction == "DOWN":
            self.coordXP += self.moveD
            if self.changeGrid:
                Character.moveDown(self)
                self.changeGrid = False
            else:
                self.changeGrid = True
        elif self.direction == "LEFT":
            self.coordYP -= self.moveD
            if self.changeGrid:
                Character.moveLeft(self)
                self.changeGrid = False
            else:
                self.changeGrid = True
        elif self.direction == "RIGHT":
            self.coordYP += self.moveD
            if self.changeGrid:
                Character.moveRight(self)
                self.changeGrid = False
            else:
                self.changeGrid = True