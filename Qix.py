from Character import Character
from random import randint

class Qix(Character):

    def __init__(self, cX, cY):
        self.moveD = 2
        Character.__init__( self, cX, cY, cX*4+92, cY*4+10, self.moveD)
        self.changeGrid = False
        self.changeD = randint(40,80)
        while (self.changeD % 2 != 0):
            self.changeD = randint(40,80)
        #print (self.changeGrid)
        self.direction = self.randDirection(8)
    
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
        if rand == 5:
            return "UR"
        if rand == 6:
            return "UL"
        if rand == 7:
            return "DL"
        if rand == 8:
            return "DR"


    #this for some reason isnt working
    #if i fux player and this still doesnt work then fix this
    #problem is it doesnt detect a wall
    def checkWall(self, g, p):
        if self.coordYGrid < 69:
            if g.getGrid(self.coordXGrid,self.coordYGrid+1) == 1:
                if [self.coordXGrid, self.coordYGrid+1] in p.getDraw():
                    self.checkCollision(p, g)
                return True
        if self.coordYGrid > 0:
            if g.getGrid(self.coordXGrid,self.coordYGrid-1) == 1:
                if [self.coordXGrid, self.coordYGrid-1] in p.getDraw():
                    self.checkCollision(p, g)
                return True
        if self.coordXGrid < 69:
            if g.getGrid(self.coordXGrid+1,self.coordYGrid) == 1:
                if [self.coordXGrid+1, self.coordYGrid] in p.getDraw():
                    self.checkCollision(p, g)
                return True
        if self.coordXGrid > 0:
            if g.getGrid(self.coordXGrid-1,self.coordYGrid) == 1:
                if [self.coordXGrid-1, self.coordYGrid] in p.getDraw():
                    self.checkCollision(p, g)
                return True
        return False

    def checkIntersection(self, g):
        options = []
        if self.coordYGrid < 69:
            if g.getGrid(self.coordXGrid,self.coordYGrid+1) == 0:
                options.append("RIGHT")
        if self.coordYGrid > 0:
            if g.getGrid(self.coordXGrid,self.coordYGrid-1) == 0:
                options.append("LEFT")
        if self.coordXGrid < 69:
            if g.getGrid(self.coordXGrid+1,self.coordYGrid) == 0:
                options.append("DOWN")
        if self.coordXGrid > 0:
            if g.getGrid(self.coordXGrid-1,self.coordYGrid) == 0:
                options.append("UP")
        if "UP" in options and "LEFT" in options:
            options.append("UL")
        if "UP" in options and "RIGHT" in options:
            options.append("UR")
        if "DOWN" in options and "LEFT" in options:
            options.append("DL")
        if "DOWN" in options and "RIGHT" in options:
            options.append("DR")
        return options

    def move(self, g, p):
        options = self.checkIntersection(g)
        if self.checkWall(g, p) and not self.changeGrid:
            self.changeD = 0
        if self.changeD == 0:
            self.direction = options[randint(0, len(options)-1)]
            self.changeD = randint(40,80)
            while (self.changeD % 2 != 0):
                self.changeD = randint(40,80)
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
        elif self.direction == "UL":
            self.coordYP -= self.moveD
            self.coordXP -= self.moveD
            self.changeD -=1
            if self.changeGrid:
                Character.moveUp(self)
                Character.moveLeft(self)
                self.changeGrid = False
            else:
                self.changeGrid = True
        elif self.direction == "UR":
            self.coordYP += self.moveD
            self.coordXP -= self.moveD
            self.changeD -=1
            if self.changeGrid:
                Character.moveUp(self)
                Character.moveRight(self)
                self.changeGrid = False
            else:
                self.changeGrid = True
        elif self.direction == "DR":
            self.coordYP += self.moveD
            self.coordXP += self.moveD
            self.changeD -=1
            if self.changeGrid:
                Character.moveDown(self)
                Character.moveRight(self)
                self.changeGrid = False
            else:
                self.changeGrid = True
        elif self.direction == "DL":
            self.coordYP -= self.moveD
            self.coordXP += self.moveD
            self.changeD -=1
            if self.changeGrid:
                Character.moveDown(self)
                Character.moveLeft(self)
                self.changeGrid = False
            else:
                self.changeGrid = True
    
    def checkCollision(self, p, g):
        p.qixHit(g)