from Character import Character

class Player(Character):

    def __init__(self, cX, cY):
        self.moveD = 4
        self.moveDS = 2
        Character.__init__( self, cX, cY, cX*4 + 92, cY*4 +12, self.moveD)
        self.lifeForce = 3
        self.Draw = []
        self.currentSlow = None
        self.changeGrid = False
        self.currentDirection = None

    #fix that fact that the draws are deleting themselves after they are done. This is stopping qix from hitting them and from thema allowing to travese it back
    def move(self, UP, DOWN, LEFT, RIGHT, DRAW, SLOW, g, q):
        if (DRAW and g.getGrid(self.coordXGrid, self.coordYGrid) == 1) or DRAW == False:
            if len(self.Draw) == 0:
                if UP and self.coordXGrid > 0: 
                    if g.getGrid(self.coordXGrid-1, self.coordYGrid) == 1:
                        self.coordXP -= self.moveD
                        Character.moveUp(self)
                        return
                elif DOWN and self.coordXGrid < 69:
                    if g.getGrid(self.coordXGrid+1, self.coordYGrid) == 1:
                        self.coordXP += self.moveD
                        Character.moveDown(self)
                        return
                elif LEFT and self.coordYGrid > 0:
                    if g.getGrid(self.coordXGrid, self.coordYGrid-1) == 1:
                        self.coordYP -= self.moveD
                        Character.moveLeft(self)
                        return
                elif RIGHT and self.coordYGrid < 69:
                    if g.getGrid(self.coordXGrid, self.coordYGrid+1) == 1:
                        self.coordYP += self.moveD
                        Character.moveRight(self)
                        return
        if DRAW:
            if len(self.Draw) == 0:
                self.currentSlow = SLOW
            if self.currentSlow and not self.changeGrid:
                if not SLOW:
                    self.currentSlow = SLOW
                    self.switchSpeed(self.Draw, g)
            if not self.changeGrid:
                if UP:
                    self.currentDirection = "u"
                elif DOWN:
                    self.currentDirection = "d"
                elif LEFT:
                    self.currentDirection = "l"
                elif RIGHT:
                    self.currentDirection = "r"
            if self.currentSlow:
                if self.currentDirection == "u" and self.coordXGrid > 0:
                    if (g.getGrid(self.coordXGrid-1, self.coordYGrid) == 0 or g.getGrid(self.coordXGrid-1, self.coordYGrid) == 1) and not [self.coordXGrid-1, self.coordYGrid] in self.Draw:
                        self.coordXP -= self.moveDS
                        if self.changeGrid:
                            Character.moveUp(self)                    
                            self.Draw.append([self.coordXGrid, self.coordYGrid])
                            if g.getGrid(self.coordXGrid, self.coordYGrid) == 1:
                                if g.updateGridBox(self.Draw, self.currentSlow, q):
                                    return True
                                self.Draw = []
                                self.currentSlow = None
                                self.changeGrid = False
                                return
                            g.updateGridLine(self.coordXGrid, self.coordYGrid, "r")
                            self.changeGrid = False
                        else:
                            self.changeGrid = True
                    if (g.getGrid(self.coordXGrid-1, self.coordYGrid) == 0 or g.getGrid(self.coordXGrid-1, self.coordYGrid) == 1) and [self.coordXGrid-1, self.coordYGrid] in self.Draw:
                        self.hitSelf(g)
                elif self.currentDirection == "d" and self.coordXGrid < 69:
                    if (g.getGrid(self.coordXGrid+1, self.coordYGrid) == 0 or g.getGrid(self.coordXGrid+1, self.coordYGrid) == 1) and not [self.coordXGrid+1, self.coordYGrid] in self.Draw:
                        self.coordXP += self.moveDS
                        if self.changeGrid:
                            Character.moveDown(self)
                            self.Draw.append([self.coordXGrid, self.coordYGrid])
                            if g.getGrid(self.coordXGrid, self.coordYGrid) == 1:
                                if g.updateGridBox(self.Draw, self.currentSlow, q):
                                    return True
                                self.Draw = []
                                self.currentSlow = None
                                self.changeGrid = False
                                return
                            g.updateGridLine(self.coordXGrid, self.coordYGrid, "r")
                            self.changeGrid = False
                        else:
                            self.changeGrid = True
                    if (g.getGrid(self.coordXGrid+1, self.coordYGrid) == 0 or g.getGrid(self.coordXGrid+1, self.coordYGrid) == 1) and [self.coordXGrid+1, self.coordYGrid] in self.Draw:
                        self.hitSelf(g)
                elif self.currentDirection == "l" and self.coordYGrid > 0:
                    if (g.getGrid(self.coordXGrid, self.coordYGrid-1) == 0 or g.getGrid(self.coordXGrid, self.coordYGrid-1) == 1) and not [self.coordXGrid, self.coordYGrid-1] in self.Draw:
                        self.coordYP -= self.moveDS
                        if self.changeGrid:
                            Character.moveLeft(self)                    
                            self.Draw.append([self.coordXGrid, self.coordYGrid])
                            if g.getGrid(self.coordXGrid, self.coordYGrid) == 1:
                                if g.updateGridBox(self.Draw, self.currentSlow, q):
                                    return True
                                self.Draw = []
                                self.currentSlow = None
                                self.changeGrid = False
                                return
                            g.updateGridLine(self.coordXGrid, self.coordYGrid, "r")
                            self.changeGrid = False
                        else:
                            self.changeGrid = True
                    if (g.getGrid(self.coordXGrid, self.coordYGrid-1) == 0 or g.getGrid(self.coordXGrid, self.coordYGrid-1) == 1) and [self.coordXGrid, self.coordYGrid-1] in self.Draw:
                        self.hitSelf(g)
                elif self.currentDirection == "r" and self.coordYGrid < 69:
                    if (g.getGrid(self.coordXGrid, self.coordYGrid+1) == 0 or g.getGrid(self.coordXGrid, self.coordYGrid+1) == 1) and not [self.coordXGrid, self.coordYGrid+1] in self.Draw:
                        self.coordYP += self.moveDS
                        if self.changeGrid:
                            Character.moveRight(self)
                            self.Draw.append([self.coordXGrid, self.coordYGrid])
                            if g.getGrid(self.coordXGrid, self.coordYGrid) == 1:
                                if g.updateGridBox(self.Draw, self.currentSlow, q):
                                    return True
                                self.Draw = []
                                self.currentSlow = None
                                self.changeGrid = False
                                return
                            g.updateGridLine(self.coordXGrid, self.coordYGrid, "r")
                            self.changeGrid = False
                        else:
                            self.changeGrid = True
                    if (g.getGrid(self.coordXGrid, self.coordYGrid+1) == 0 or g.getGrid(self.coordXGrid, self.coordYGrid+1) == 1) and [self.coordXGrid, self.coordYGrid+1] in self.Draw:
                        self.hitSelf(g)
            else:
                if UP and self.coordXGrid > 0: 
                    if (g.getGrid(self.coordXGrid-1, self.coordYGrid) == 0 or g.getGrid(self.coordXGrid-1, self.coordYGrid) == 1) and not [self.coordXGrid-1, self.coordYGrid] in self.Draw:
                        self.coordXP -= self.moveD
                        Character.moveUp(self)                    
                        self.Draw.append([self.coordXGrid, self.coordYGrid])
                        if g.getGrid(self.coordXGrid, self.coordYGrid) == 1:
                            if g.updateGridBox(self.Draw, self.currentSlow, q):
                                    return True
                            self.Draw = []
                            self.currentSlow = None
                            return
                        g.updateGridLine(self.coordXGrid, self.coordYGrid, "b")
                    if (g.getGrid(self.coordXGrid-1, self.coordYGrid) == 0 or g.getGrid(self.coordXGrid-1, self.coordYGrid) == 1) and [self.coordXGrid-1, self.coordYGrid] in self.Draw:
                        self.hitSelf(g)
                elif DOWN and self.coordXGrid < 69:
                    if (g.getGrid(self.coordXGrid+1, self.coordYGrid) == 0 or g.getGrid(self.coordXGrid+1, self.coordYGrid) == 1) and not [self.coordXGrid+1, self.coordYGrid] in self.Draw:
                        self.coordXP += self.moveD
                        Character.moveDown(self)
                        self.Draw.append([self.coordXGrid, self.coordYGrid])
                        if g.getGrid(self.coordXGrid, self.coordYGrid) == 1:
                            if g.updateGridBox(self.Draw, self.currentSlow, q):
                                    return True
                            self.Draw = []
                            self.currentSlow = None
                            return
                        g.updateGridLine(self.coordXGrid, self.coordYGrid, "b")
                    if (g.getGrid(self.coordXGrid+1, self.coordYGrid) == 0 or g.getGrid(self.coordXGrid+1, self.coordYGrid) == 1) and [self.coordXGrid+1, self.coordYGrid] in self.Draw:
                        self.hitSelf(g)
                elif LEFT and self.coordYGrid > 0:
                    if (g.getGrid(self.coordXGrid, self.coordYGrid-1) == 0 or g.getGrid(self.coordXGrid, self.coordYGrid-1) == 1) and not [self.coordXGrid, self.coordYGrid-1] in self.Draw:
                        self.coordYP -= self.moveD
                        Character.moveLeft(self)                    
                        self.Draw.append([self.coordXGrid, self.coordYGrid])
                        if g.getGrid(self.coordXGrid, self.coordYGrid) == 1:
                            if g.updateGridBox(self.Draw, self.currentSlow, q):
                                    return True
                            self.Draw = []
                            self.currentSlow = None
                            return
                        g.updateGridLine(self.coordXGrid, self.coordYGrid, "b")
                    if (g.getGrid(self.coordXGrid, self.coordYGrid-1) == 0 or g.getGrid(self.coordXGrid, self.coordYGrid-1) == 1) and [self.coordXGrid, self.coordYGrid-1] in self.Draw:
                        self.hitSelf(g)
                elif RIGHT and self.coordYGrid < 69:
                    if (g.getGrid(self.coordXGrid, self.coordYGrid+1) == 0 or g.getGrid(self.coordXGrid, self.coordYGrid+1) == 1) and not [self.coordXGrid, self.coordYGrid+1] in self.Draw:
                        self.coordYP += self.moveD
                        Character.moveRight(self)
                        self.Draw.append([self.coordXGrid, self.coordYGrid])
                        if g.getGrid(self.coordXGrid, self.coordYGrid) == 1:
                            if g.updateGridBox(self.Draw, self.currentSlow, q):
                                    return True
                            self.Draw = []
                            self.currentSlow = None
                            return
                        g.updateGridLine(self.coordXGrid, self.coordYGrid, "b")
                    if (g.getGrid(self.coordXGrid, self.coordYGrid+1) == 0 or g.getGrid(self.coordXGrid, self.coordYGrid+1) == 1) and [self.coordXGrid, self.coordYGrid+1] in self.Draw:
                        self.hitSelf(g)
    
    def checkLoseLife(self, x, y):
        if x == self.coordXGrid and y == self.coordYGrid:
            self.lifeForce -= 1
            self.coordXGrid = 0
            self.coordYGrid = 0
            self.coordXP = 0*4 +92
            self.coordYP = 0*4 +12
            for i in range(100):
                for j in range(100):
                    if [i,j] in self.Draw:
                        g.setGrid(i,j, 0)
                        g.setCGrid(i,j,None)
            self.Draw = []
    
    def getDraw(self):
        return self.Draw

    #create new one hit self for player class so it works in sequence diagram
    def qixHit(self,g):
        self.lifeForce -=1
        self.coordXGrid = 0
        self.coordYGrid = 0
        self.coordXP = self.coordXGrid*4 + 92
        if self.coordYGrid == 0:
            self.coordYP = self.coordYGrid*4 +12
        else:
            self.coordYP = self.coordYGrid*4 +10
        for i in range(100):
            for j in range(100):
                if [i,j] in self.Draw:
                    g.setGrid(i,j, 0)
                    g.setCGrid(i,j,None)
        self.Draw = []

    def hitSelf(self,g):
        self.lifeForce -=1
        self.coordXGrid = 0
        self.coordYGrid = 0
        self.coordXP = self.coordXGrid*4 + 92
        if self.coordYGrid == 0:
            self.coordYP = self.coordYGrid*4 +12
        else:
            self.coordYP = self.coordYGrid*4 +10
        for i in range(100):
            for j in range(100):
                if [i,j] in self.Draw:
                    g.setGrid(i,j, 0)
                    g.setCGrid(i,j,None)
        self.Draw = []
    
    def switchSpeed(self, draw, g):
        for i in draw:
            g.setCGrid(i[0],i[1], "b")
    
    def getLife(self):
        return self.lifeForce