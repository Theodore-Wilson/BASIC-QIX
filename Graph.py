class Graph:

    #contructer for Graph class
    #the play area is only 70 by 70
    #the extra row and columns i to account for the edges which are traversable by the characters
    #grid is created in a scale of 1/10 to the pixel count
    def __init__ (self):
        self.grid = [[0 for i in range (70)] for i in range (70)]
        self.cGrid = [[None for i in range (70)] for i in range (70)]
        self.currentPercent = 0
        self.accessibleWalls = []

    def setupGrid(self):
        for i in range (70):
            self.grid[i][0] = 1
            self.cGrid[i][0] = "w"
            self.grid[i][69] = 1
            self.cGrid[i][69] = "w"
            self.grid[0][i] = 1
            self.cGrid[0][i] = "w"
            self.grid[69][i] =1
            self.cGrid[69][i] = "w"
        self.updateWalls()
    
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
    def updateGridBox(self, draw, slow, q):
        for i in draw:
            self.cGrid[i[0]][i[1]] = "w" 
        qT = (q[0], q[1])
        qixArea = [qT]
        visited = {qT}
        
        for q in qixArea:
            temp = (q[0] +1,q[1])
            if temp not in visited:
                if self.grid[q[0] +1][q[1]] == 0:
                    qixArea.append(temp)
            temp = (q[0] -1,q[1])
            if temp not in visited:
                if self.grid[q[0]-1][q[1]] == 0:
                    qixArea.append(temp)
            temp = (q[0],q[1]-1)
            if temp not in visited:
                if self.grid[q[0]][q[1]-1] == 0:
                    qixArea.append(temp)
            temp = (q[0],q[1]+1)
            if temp not in visited:
                if self.grid[q[0]][q[1]+1] == 0:
                    qixArea.append(temp)
            visited.update(qixArea)

        for i in range(1,69):
            for j in range(1,69):
                if self.grid[i][j] == 0 and (i,j) not in visited:
                    if slow:
                        self.grid[i][j] = 3
                        self.cGrid[i][j] = "r"
                    else:
                        self.grid[i][j] = 2
                        self.cGrid[i][j] = "b"

        self.updateWalls()
        if self.checkWin():
            return True

    #finish writing this tomorrow
    def updateWalls(self):
        self.accessibleWalls = []
        for i in range(70):
            for j in range(70):
                count = 0
                if self.grid[i][j] == 1:
                    if i < 69 and j < 69:
                        if self.grid[i+1][j+1] != 0:
                            count +=1
                    if i > 0 and j < 69:
                        if self.grid[i-1][j+1] != 0:
                            count +=1
                    if i < 69 and j > 0:
                        if self.grid[i+1][j-1] != 0:
                            count +=1
                    if i > 0 and j > 0:
                        if self.grid[i-1][j-1] != 0:
                            count +=1
                    if j < 69:
                        if self.grid[i][j+1] != 0:
                            count +=1
                    if j > 0:
                        if self.grid[i][j-1] != 0:
                            count +=1
                    if i < 69:
                        if self.grid[i+1][j] != 0:
                            count +=1
                    if i > 0:
                        if self.grid[i-1][j] != 0:
                            count +=1
                    if i == 0 or j == 0 or i == 69 or j == 69:
                        count += 3
                    if count == 8:
                        self.grid[i][j] = 4
                    if count < 8:
                        self.accessibleWalls.append((i,j))
    
    #This will check if a player has won the game or not
    #it will take into account the percentage of the grid that they have control over
    #if it is greater then they win
    #this will only be checked every time a box is completed
    #wP is win Percent which is specified in the main function
    def checkWin(self, wP = 0.65):
        count = 0
        for i in range(1, 69):
            for j in range(1, 69):
                if self.grid[i][j] == 3:
                    count += 2
                elif self.grid[i][j] == 2:
                    count +=1
        self.currentPercent = count/(68*68)
        if count > (68*68)*wP:
            return True
        else:
            return False

    def setGrid(self, x, y, v):
        self.grid[x][y] = v

    def setCGrid(self, x, y, v):
        self.cGrid[x][y] = v
    
    def getCurrentPercent(self):
        return self.currentPercent
    
    def getEntireGrid(self):
        return self.grid
    
    def getEntireCGrid(self):
        return self.cGrid
    
    def getWalls(self):
        return self.accessibleWalls