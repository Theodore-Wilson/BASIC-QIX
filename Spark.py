from Character import Character
from random import randint

class Spark(Character):

    def __init__(self, cX, cY):
        self.moveD = 2
        Character.__init__( self, cX, cY, cX*4+92, cY*4+10)
        self.changeGrid = False
        self.direction = "RIGHT"

    def checkIntersection(self, g, p):
        options = [[], []]
        if self.coordYGrid < 69:
            if g.getGrid(self.coordXGrid,self.coordYGrid+1) == 1 and [self.coordXGrid,self.coordYGrid+1] not in p.getDraw():
                options[0].append("RIGHT")
            if g.getGrid(self.coordXGrid,self.coordYGrid+1) == 4:
                options[1].append("RIGHT")
        if self.coordYGrid > 0:
            if g.getGrid(self.coordXGrid,self.coordYGrid-1) == 1 and [self.coordXGrid,self.coordYGrid-1] not in p.getDraw():
                options[0].append("LEFT")
            if g.getGrid(self.coordXGrid,self.coordYGrid-1) == 4:
                options[1].append("LEFT")
        if self.coordXGrid < 69:
            if g.getGrid(self.coordXGrid+1,self.coordYGrid) == 1 and [self.coordXGrid+1,self.coordYGrid] not in p.getDraw():
                options[0].append("DOWN")
            if g.getGrid(self.coordXGrid+1,self.coordYGrid) == 4:
                options[1].append("DOWN")
        if self.coordXGrid > 0:
            if g.getGrid(self.coordXGrid-1,self.coordYGrid) == 1 and [self.coordXGrid-1,self.coordYGrid] not in p.getDraw():
                options[0].append("UP")
            if g.getGrid(self.coordXGrid-1,self.coordYGrid) == 4:
                options[1].append("UP")
        return options

    def move(self, g, p):
        if self.changeGrid:
            options = self.checkIntersection(g, p)
            if len(options[0]) > 0:
                if not(len(options[0]) == 2 and (("UP" in options[0] and "DOWN" in options[0]) or ("LEFT" in options[0] and "RIGHT" in options[0]))):
                    if len(options[0]) > 0:
                        rand = randint(0,len(options[0])-1)
                        self.direction = options[0][rand]
            else:
                if not(len(options[1]) == 2 and (("UP" in options[1] and "DOWN" in options[1]) or ("LEFT" in options[1] and "RIGHT" in options[1]))):
                    if len(options[1]) > 0:
                        rand = randint(0,len(options[1])-1)
                        self.direction = options[1][rand]
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