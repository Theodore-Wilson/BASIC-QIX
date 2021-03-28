class Character:

    def __init__(self, cX, cY, cXP, cYP, mD):
        self.coordXGrid = cX
        self.coordYGrid = cY
        self.coordXP = cXP
        self.coordYP = cYP
        self.moveDistance = mD

    def moveUp(self):
        self.coordXGrid -= 1

    def moveDown(self):    
        self.coordXGrid += 1

    def moveRight(self):
        self.coordYGrid += 1

    def moveLeft(self):
        self.coordYGrid -= 1
    
    def getCoordXGrid(self):
        return self.coordXGrid
    
    def getCoordYGrid(self):
        return self.coordYGrid
    
    def getCoordXP(self):
        return self.coordXP
    
    def getCoordYP(self):
        return self.coordYP
