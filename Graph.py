class Graph:

    #contructer for Graph class
    #creates a grid 102 by 102
    #the play area is only 100 by 100
    #the extra row and columns i to account for the edges which are traversable by the characters
    #grid is created in a scale of 1/10 to the pixel count
    #therefore game will be created in a grid 1000P by 1000P
    def __init__ (self):
        self.grid = [[0 for i in range (101)] for i in range (101)]
        self.directionGrid = [[None for i in range (101)] for i in range (101)]

    def setupGrid(self):
        for i in range (101):
            self.grid[i][0] = 1
            self.grid[i][100] = 1
            self.grid[0][i] = 1
            self.grid[100][i] =1 

    def setupDirectionGrid(self):
        for i in range (101):
            for j in range(101):
                self.directionGrid[i][j] = None
    
    def getGrid(self, x, y):
        return self.grid[x][y]

    def getDirectionGrid(self, x, y):
        return self.directionGrid[x][y]

    #updates the grid for drawn lines
    #will only be called if the correct button is pressed to initiate a line draw.
    def updateGridLine(self, xCoord, yCoord, d):
        self.grid[xCoord][yCoord] = 1
        self.directionGrid[xCoord][yCoord] = d


    #Updates the grid when a box has been drawn
    #should only be called when check completeBox is true
    def updateGridBox(self):
        self.checkCompleteBox()
        return        

    #write this later has to check if the box is complete to add towards the final goal
    #have no idea how to do this right now
    def checkCompleteBox(self):
        return
    
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