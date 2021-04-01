class Graph:

    #contructer for Graph class
    #creates a grid 102 by 102
    #the play area is only 100 by 100
    #the extra row and columns i to account for the edges which are traversable by the characters
    #grid is created in a scale of 1/10 to the pixel count
    #therefore game will be created in a grid 1000P by 1000P
    def __init__ (self):
        self.grid = [[0 for i in range (100)] for i in range (100)]
        self.cGrid = [[None for i in range (100)] for i in range (100)]

    def setupGrid(self):
        for i in range (100):
            self.grid[i][0] = 1
            self.cGrid[i][0] = "w"
            self.grid[i][99] = 1
            self.cGrid[i][99] = "w"
            self.grid[0][i] = 1
            self.cGrid[0][i] = "w"
            self.grid[99][i] =1
            self.cGrid[99][i] = "w"
    
    def getGrid(self, x, y):
        return self.grid[x][y]

    def getCGrid(self, x, y):
        return self.cGrid[x][y]

    #updates the grid for drawn lines
    #will only be called if the correct button is pressed to initiate a line draw.
    def updateGridLine(self, xCoord, yCoord, d):
        self.grid[xCoord][yCoord] = 1
        self.cGrid[xCoord][yCoord] = d


    #Updates the grid when a box has been drawn
    #should only be called when check completeBox is true
    def updateGridBox(self, draw, slow):
        if slow:
            colour = "r"
        else:
            colour = "b"
        for i in range(100):
            for j in range(100):
                if [i,j] in draw:
                    self.cGrid[i][j] = "w"        
    
    #This will check if a player has won the game or not
    #it will take into account the percentage of the grid that they have control over
    #if it is greater then they win
    #this will only be checked every time a box is completed
    #wP is win Percent which is specified in the main function
    def checkWin(self, wP):
        count = 0
        for i in range(1, 101):
            for j in range(1, 101):
                if self.grid[i][j] == 2 or self.grid[i][j] == 1:
                    count += 1
        if count > (10000*wP):
            return True
        else:
            return False

    def setGrid(self, x, y, v):
        self.grid[x][y] = v

    def setCGrid(self, x, y, v):
        self.cGrid[x][y] = v