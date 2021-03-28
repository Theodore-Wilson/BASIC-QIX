from Character import Character
from Graph import Graph

class Player(Character):

    def __init__(self, cX, cY):
        self.moveD = 10
        Character.__init__( self, cX, cY, cX*10 + 5, cY*10 +5, self.moveD)
        self.lifeForce = 300
        self.Draw = []

    def move(self, UP, DOWN, LEFT, RIGHT, DRAW, g):
        if DRAW == True:
            if UP == True and self.coordXP > 5: 
                if g.getGrid(self.coordXGrid-1, self.coordYGrid) == 0 or g.getGrid(self.coordXGrid-1, self.coordYGrid) == 1: 
                    #one more if for if its outter edge and edge is empty dont draw
                    self.coordXP -= self.moveD
                    Character.moveUp(self)
                    self.Draw.append([self.coordXGrid, self.coordYGrid])
                    g.updateGridLine(self.coordXGrid, self.coordYGrid, "VU")
                    if g.getGrid(self.coordXGrid, self.coordYGrid) == 1:
                        g.updateGridBox()
                        self.Draw = []
            elif DOWN == True and self.coordXP < 1000:
                if g.getGrid(self.coordXGrid+1, self.coordYGrid) == 0 or g.getGrid(self.coordXGrid+1, self.coordYGrid) == 1:
                    self.coordXP += self.moveD
                    Character.moveDown(self)
                    self.Draw.append([self.coordXGrid, self.coordYGrid])
                    g.updateGridLine(self.coordXGrid, self.coordYGrid, "VD")
                    if g.getGrid(self.coordXGrid, self.coordYGrid) == 1:
                        g.updateGridBox()
                        self.Draw = []
            elif LEFT == True and self.coordYP > 5:
                if g.getGrid(self.coordXGrid, self.coordYGrid-1) == 0 or g.getGrid(self.coordXGrid, self.coordYGrid-1) == 1:
                    self.coordYP -= self.moveD
                    Character.moveLeft(self)
                    self.Draw.append([self.coordXGrid, self.coordYGrid])
                    g.updateGridLine(self.coordXGrid, self.coordYGrid, "HL")
                    if g.getGrid(self.coordXGrid, self.coordYGrid) == 1:
                        g.updateGridBox()
                        self.Draw = []
            elif RIGHT == True and self.coordYP < 1000:
                if g.getGrid(self.coordXGrid, self.coordYGrid+1) == 0 or g.getGrid(self.coordXGrid, self.coordYGrid+1) == 1:
                    self.coordYP += self.moveD
                    Character.moveRight(self)
                    self.Draw.append([self.coordXGrid, self.coordYGrid])
                    g.updateGridLine(self.coordXGrid, self.coordYGrid, "HR")
                    if g.getGrid(self.coordXGrid, self.coordYGrid) == 1:
                        g.updateGridBox()
                        self.Draw = []
            #g.updateGridLine(self.coordXGrid, self.coordYGrid)
        else:
            if UP == True and self.coordXP > 5: 
                if g.getGrid(self.coordXGrid-1, self.coordYGrid) == 1:
                    self.coordXP -= self.moveD
                    Character.moveUp(self)
            elif DOWN == True and self.coordXP < 1000:
                if g.getGrid(self.coordXGrid+1, self.coordYGrid) == 1:
                    self.coordXP += self.moveD
                    Character.moveDown(self)
            elif LEFT == True and self.coordYP > 5:
                if g.getGrid(self.coordXGrid, self.coordYGrid-1) == 1:
                    self.coordYP -= self.moveD
                    Character.moveLeft(self)
            elif RIGHT == True and self.coordYP < 1000:
                if g.getGrid(self.coordXGrid, self.coordYGrid+1) == 1:
                    self.coordYP += self.moveD
                    Character.moveRight(self)
        #print (self.coordXGrid)
        #print (self.coordYGrid)
        #print ()
    
    def checkLoseLife(self, x, y):
        if x == self.coordXGrid and y == self.coordYGrid:
            self.lifeForce -= 100
            self.coordXGrid = 0
            self.coordYGrid = 0
            self.coordXP = 5
            self.coordYP = 5
    
    def getDraw(self):
        return self.Draw