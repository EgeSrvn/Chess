import copy as cpy

class piece:
    def __init__(self, side, x, y):
        self.side = side
        self.x = x
        self.y = y
        self.available = True
        self.tempEaten = False
    
    def move(self, mx, my):
        self.x = mx
        self.y = my
    
#################################################
class pawn(piece):
    def __init__(self, side, x, y):
        piece.__init__(self, side, x, y)
        self.notMoved = True
        if side == 1:
            self.name = "bpawn"
        else:
            self.name = "wpawn"
        
    def move(self, mx, my):
        piece.move(self, mx, my)
        self.notMoved = True
    
    def availableSquares(self, Cboard, pieces, king):
        squares = [[False for i in range(8)] for j in range(8)]
        availables = list()

        if self.side == 1:
            if self.y > 1 and self.notMoved and Cboard[self.x][self.y-1] == None and Cboard[self.x][self.y-2] == None:
                squares[self.x][self.y-2] = True
                
            if self.y > 0 and Cboard[self.x][self.y-1] == None:
                squares[self.x][self.y-1] = True
                
            if self.x+1 < 8 and self.y > 0 and Cboard[self.x+1][self.y-1] != None and Cboard[self.x+1][self.y-1].side != self.side:
                squares[self.x+1][self.y-1] = True
            
            if self.x-1 > -1 and self.y > 0 and Cboard[self.x-1][self.y-1] != None and Cboard[self.x-1][self.y-1].side != self.side:
                squares[self.x-1][self.y-1] = True
        
        if self.side == 0:
            if self.y < 6 and self.notMoved and Cboard[self.x][self.y+1] == None and Cboard[self.x][self.y+2] == None:
                squares[self.x][self.y+2] = True
                
            if self.y < 7 and Cboard[self.x][self.y+1] == None:
                squares[self.x][self.y+1] = True
                
            if self.x+1 < 8 and self.y < 7 and Cboard[self.x+1][self.y+1] != None and Cboard[self.x+1][self.y+1].side != self.side:
                squares[self.x+1][self.y+1] = True
            
            if self.x-1 > -1 and self.y < 7 and Cboard[self.x-1][self.y+1] != None and Cboard[self.x-1][self.y+1].side != self.side:
                squares[self.x-1][self.y+1] = True

        for i in range(8):
            for j in range(8):
                if squares[i][j] == True:
                    tempBoard = cpy.deepcopy(Cboard)
                    temp = tempBoard[self.x][self.y]
                    tempBoard[self.x][self.y] = None

                    tempPieces = cpy.copy(pieces)

                    tempBoard[i][j] = temp
                    temp.x = i
                    temp.y = j

                    tempPieces.remove(self)
                    tempPieces.append(temp)

                    if Cboard[i][j] != None:
                        Cboard[i][j].tempEaten = True

                    if not king.canBeEaten(king.x, king.y, tempBoard, tempPieces):
                        availables.append([i, j])

                    if Cboard[i][j] != None:
                        Cboard[i][j].tempEaten = False

        return availables
    
    def canReach(self, Cboard, coordinate):
        cx = coordinate[0]
        cy = coordinate[1]
        
        diffx = abs(cx - self.x)
        diffy = abs(cy - self.y)
        
        if diffx != 1 and diffy != 1:
            return False
        else:
            if self.side == 1:
                if (cx == self.x-1 or cx == self.x+1) and cy == self.y-1:
                    return True
                else:
                    return False
            else:
                if (cx == self.x-1 or cx == self.x+1) and cy == self.y+1:
                    return True
                else:
                    return False
            
                 
        
#################################################
class rook(piece):
    def __init__(self, side, x, y):
        piece.__init__(self, side, x, y)
        self.notMoved = True
        if side == 1:
            self.name = "brook"
        else:
            self.name = "wrook"
        
    def move(self, mx, my):
        piece.move(self, mx, my)
        self.notMoved = False
        
    def availableSquares(self, Cboard, pieces, king):
        squares = [[False for i in range(8)] for j in range(8)]
        availables = list()
        
        if self.x != 0:
            currX = self.x-1
            currY = self.y
            curr = Cboard[currX][currY]
            finished = False
            while(currX != -1 and (curr == None or (curr.side != self.side)) and not finished):
                if curr != None and curr.side != self.side:
                    squares[currX][currY] = True
                    finished = True
                squares[currX][currY] = True
                currX -= 1
                if currX != -1:
                    curr = Cboard[currX][currY]
          
        if self.x != 7:
            currX = self.x+1
            currY = self.y
            curr = Cboard[currX][currY]
            finished = False
            while(currX != 8 and (curr == None or (curr.side != self.side)) and not finished):
                if curr != None and curr.side != self.side:
                    squares[currX][currY] = True
                    finished = True
                squares[currX][currY] = True
                currX += 1
                if currX != 8:
                    curr = Cboard[currX][currY]
                                   
        if self.y != 0:
            currX = self.x
            currY = self.y-1
            curr = Cboard[currX][currY]
            finished = False
            while(currY != -1 and (curr == None or (curr.side != self.side)) and not finished):
                curr = Cboard[currX][currY]
                if curr != None and curr.side != self.side:
                    squares[currX][currY] = True
                    finished = True
                squares[currX][currY] = True
                currY -= 1
                if currY != -1:
                    curr = Cboard[currX][currY]
                      
        if self.y != 7:
            currX = self.x
            currY = self.y+1
            curr = Cboard[currX][currY]
            finished = False
            while(currY != 8 and (curr == None or (curr.side != self.side)) and not finished):
                if curr != None and curr.side != self.side:
                    squares[currX][currY] = True
                    finished = True
                squares[currX][currY] = True
                currY += 1
                if currY != 8:
                    curr = Cboard[currX][currY]

        for i in range(8):
            for j in range(8):
                if squares[i][j] == True:
                    tempBoard = cpy.deepcopy(Cboard)
                    temp = tempBoard[self.x][self.y]
                    tempBoard[self.x][self.y] = None

                    tempPieces = cpy.copy(pieces)

                    tempBoard[i][j] = temp
                    temp.x = i
                    temp.y = j

                    tempPieces.remove(self)
                    tempPieces.append(temp)

                    if Cboard[i][j] != None:
                        Cboard[i][j].tempEaten = True

                    if not king.canBeEaten(king.x, king.y, tempBoard, tempPieces):
                        availables.append([i, j])

                    if Cboard[i][j] != None:
                        Cboard[i][j].tempEaten = False
            
        return availables
    
    def canReach(self, Cboard, coordinate):
        cx = coordinate[0]
        cy = coordinate[1]
        
        diffx = abs(cx - self.x)
        diffy = abs(cy - self.y)
        
        if diffx != 0 and diffy != 0:
            return False
        
        if diffx != 0:
            if self.x > cx:
                currX = self.x-1
                currY = self.y
                curr = Cboard[currX][currY]
                while(curr == None and currX > -1 and currX != cx):
                    currX -= 1
                    if currX != -1:
                        curr = Cboard[currX][currY]
                if currX == cx and currY == cy:
                    return True
                
            if self.x < cx:
                currX = self.x+1
                currY = self.y
                curr = Cboard[currX][currY]
                while(curr == None and currX < 8 and currX != cx):
                    currX += 1
                    if currX != 8:
                        curr = Cboard[currX][currY]
                if currX == cx and currY == cy:
                    return True
        else:
            if self.y > cy:
                currX = self.x
                currY = self.y-1
                curr = Cboard[currX][currY]
                while(curr == None and currY > -1 and currY != cy):
                    currY -= 1
                    if currY != -1:
                        curr = Cboard[currX][currY]
                if currX == cx and currY == cy:
                    return True
                
            if self.y < cy:
                currX = self.x
                currY = self.y+1
                curr = Cboard[currX][currY]
                while(curr == None and currY < 8 and currY != cy):
                    currY += 1
                    if currY != 8:
                        curr = Cboard[currX][currY]
                if currX == cx and currY == cy:
                    return True
        return False
        
#################################################   
class knight(piece):
    def __init__(self, side, x, y):
        piece.__init__(self, side, x, y)
        if side == 1:
            self.name = "bknight"
        else:
            self.name = "wknight"
        
    def move(self, mx, my):
        piece.move(self, mx, my)
    
    def availableSquares(self, Cboard, pieces, king):
        squares = [[False for i in range(8)] for j in range(8)]
        availables = list()

        if self.x > 1 and self.y < 7:
            if Cboard[self.x-2][self.y+1] == None or Cboard[self.x-2][self.y+1].side != self.side:
                squares[self.x-2][self.y+1] = True
        
        if self.x > 0 and self.y < 6:
            if Cboard[self.x-1][self.y+2] == None or Cboard[self.x-1][self.y+2].side != self.side:
                squares[self.x-1][self.y+2] = True
        
        if self.x < 6 and self.y < 7:
            if Cboard[self.x+2][self.y+1] == None or Cboard[self.x+2][self.y+1].side != self.side:
                squares[self.x+2][self.y+1] = True
        
        if self.x < 7 and self.y < 6:
            if Cboard[self.x+1][self.y+2] == None or Cboard[self.x+1][self.y+2].side != self.side:
                squares[self.x+1][self.y+2] = True
        
        if self.x > 1 and self.y > 0:
            if Cboard[self.x-2][self.y-1] == None or Cboard[self.x-2][self.y-1].side != self.side:
                squares[self.x-2][self.y-1] = True
        
        if self.x > 0 and self.y > 1:
            if Cboard[self.x-1][self.y-2] == None or Cboard[self.x-1][self.y-2].side != self.side:
                squares[self.x-1][self.y-2] = True
        
        if self.x < 6 and self.y > 0:
            if Cboard[self.x+2][self.y-1] == None or Cboard[self.x+2][self.y-1].side != self.side:
                squares[self.x+2][self.y-1] = True
        
        if self.x < 7 and self.y > 1:
            if Cboard[self.x+1][self.y-2] == None or Cboard[self.x+1][self.y-2].side != self.side:
                squares[self.x+1][self.y-2] = True

        for i in range(8):
            for j in range(8):
                if squares[i][j] == True:
                    tempBoard = cpy.deepcopy(Cboard)
                    temp = tempBoard[self.x][self.y]
                    tempBoard[self.x][self.y] = None

                    tempPieces = cpy.copy(pieces)

                    tempBoard[i][j] = temp
                    temp.x = i
                    temp.y = j

                    tempPieces.remove(self)
                    tempPieces.append(temp)

                    if Cboard[i][j] != None:
                        Cboard[i][j].tempEaten = True

                    if not king.canBeEaten(king.x, king.y, tempBoard, tempPieces):
                        availables.append([i, j])

                    if Cboard[i][j] != None:
                        Cboard[i][j].tempEaten = False

        return availables
        
    def canReach(self, Cboard, coordinate):
        cx = coordinate[0]
        cy = coordinate[1]
        
        if self.x > 1 and self.y < 7:
            if self.x-2 == cx and self.y+1 == cy:
                return True
        
        if self.x > 0 and self.y < 6:
            if self.x-1== cx and self.y+2 == cy:
                return True
        
        if self.x < 6 and self.y < 7:
            if self.x+2 == cx and self.y+1 == cy:
                return True
        
        if self.x < 7 and self.y < 6:
            if self.x+1 == cx and self.y+2 == cy:
                return True
            
        if self.x > 1 and self.y > 0:
            if self.x-2 == cx and self.y-1 == cy:
                return True
        
        if self.x > 0 and self.y > 1:
            if self.x-1 == cx and self.y-2 == cy:
                return True
            
        if self.x < 6 and self.y > 0:
            if self.x+2 == cx and self.y-1 == cy:
                return True
        
        if self.x < 7 and self.y > 1:
            if self.x+1 == cx and self.y-2 == cy:
                return True
        
        return False
#################################################        
class bishop(piece):
    def __init__(self, side, x, y):
        piece.__init__(self, side, x, y)
        if side == 1:
            self.name = "bbishop"
        else:
            self.name = "wbishop"
        
    def move(self, mx, my):
        piece.move(self, mx, my)
        
    def availableSquares(self, Cboard, pieces, king):
        squares = [[False for i in range(8)] for j in range(8)]
        availables = list()

        if self.x > 0 and self.y > 0:
            currX = self.x - 1
            currY = self.y - 1

            curr = Cboard[currX][currY]
            finished = False

            while (not finished and (currX > -1 and currY > -1) and (curr == None or (curr.side != self.side))):
                if curr != None and curr.side != self.side:
                    squares[currX][currY] = True
                    finished = True
                squares[currX][currY] = True
                currX -= 1
                currY -= 1
                if currX != -1 and currY != -1:
                    curr = Cboard[currX][currY]

        if self.x < 7 and self.y > 0:
            currX = self.x + 1
            currY = self.y - 1

            curr = Cboard[currX][currY]
            finished = False

            while (not finished and (currX < 8 and currY > -1) and (curr == None or (curr.side != self.side))):
                if curr != None and curr.side != self.side:
                    squares[currX][currY] = True
                    finished = True
                squares[currX][currY] = True
                currX += 1
                currY -= 1
                if currX != 8 and currY != -1:
                    curr = Cboard[currX][currY]

        if self.x < 7 and self.y < 7:
            currX = self.x + 1
            currY = self.y + 1

            curr = Cboard[currX][currY]
            finished = False

            while (not finished and (currX < 8 and currY < 8) and (curr == None or (curr.side != self.side))):
                if curr != None and curr.side != self.side:
                    squares[currX][currY] = True
                    finished = True
                squares[currX][currY] = True
                currX += 1
                currY += 1
                if currX != 8 and currY != 8:
                    curr = Cboard[currX][currY]

        if self.x > 0 and self.y < 7:
            currX = self.x - 1
            currY = self.y + 1

            curr = Cboard[currX][currY]
            finished = False

            while (not finished and (currX > -1 and currY < 8) and (curr == None or (curr.side != self.side))):
                if curr != None and curr.side != self.side:
                    squares[currX][currY] = True
                    finished = True
                squares[currX][currY] = True
                currX -= 1
                currY += 1
                if currX != -1 and currY != 8:
                    curr = Cboard[currX][currY]

        for i in range(8):
            for j in range(8):
                if squares[i][j] == True:
                    tempBoard = cpy.deepcopy(Cboard)
                    temp = tempBoard[self.x][self.y]
                    tempBoard[self.x][self.y] = None

                    tempPieces = cpy.copy(pieces)

                    tempBoard[i][j] = temp
                    temp.x = i
                    temp.y = j

                    tempPieces.remove(self)
                    tempPieces.append(temp)

                    if Cboard[i][j] != None:
                        Cboard[i][j].tempEaten = True

                    if not king.canBeEaten(king.x, king.y, tempBoard, tempPieces):
                        availables.append([i, j])

                    if Cboard[i][j] != None:
                        Cboard[i][j].tempEaten = False
                    
        return availables
    
    def canReach(self, Cboard, coordinate):
        cx = coordinate[0]
        cy = coordinate[1]
        
        if self.x != 0 and self.y != 0:
            currX = self.x-1
            currY = self.y-1
            
            curr = Cboard[currX][currY]       
                
            while(curr == None and currX > -1 and currY > -1 and currX != cx and currY != cy):
                currX -= 1
                currY -= 1
                if currX != -1 and currY != -1:
                    curr = Cboard[currX][currY]
            
            if currX == cx and currY == cy:
                return True
                    
                 
        if self.x != 7 and self.y != 0:
            currX = self.x+1
            currY = self.y-1
            
            curr = Cboard[currX][currY]       
                
            while(curr == None and currX < 8 and currY > -1 and currX != cx and currY != cy):
                currX += 1
                currY -= 1
                if currX != 8 and currY != -1:
                    curr = Cboard[currX][currY]
            
            if currX == cx and currY == cy:
                return True
        
        
        if self.x != 7 and self.y != 7:
            currX = self.x+1
            currY = self.y+1
            
            curr = Cboard[currX][currY]       
                
            while(curr == None and currX < 8 and currY < 8 and currX != cx and currY != cy):
                currX += 1
                currY += 1
                if currX != 8 and currY != 8:
                    curr = Cboard[currX][currY]
                
            if currX == cx and currY == cy:
                return True
        
        
        if self.x != 0 and self.y != 7:
            currX = self.x-1
            currY = self.y+1
            
            curr = Cboard[currX][currY]       
                
            while(curr == None and currX > -1 and currY < 8 and currX != cx and currY != cy):
                currX -= 1
                currY += 1
                if currX != -1 and currY != 8:
                    curr = Cboard[currX][currY]
            
            if currX == cx and currY == cy:
                return True
        
        return False
        
#################################################        
class queen(piece):
    def __init__(self, side, x, y):
        piece.__init__(self, side, x, y)
        if side == 1:
            self.name = "bqueen"
        else:
            self.name = "wqueen"
        
    def move(self, mx, my):
        piece.move(self, mx, my)       
    
    def availableSquares(self, Cboard, pieces, king):
        squares = [[False for i in range(8)] for j in range(8)]
        availables = list()
        
        self.diagonalAvailable(squares, Cboard)
        self.orthogonalAvailable(squares, Cboard)

        for i in range(8):
            for j in range(8):
                if squares[i][j] == True:
                    tempBoard = cpy.deepcopy(Cboard)
                    temp = tempBoard[self.x][self.y]
                    tempBoard[self.x][self.y] = None

                    tempPieces = cpy.copy(pieces)

                    tempBoard[i][j] = temp
                    temp.x = i
                    temp.y = j

                    tempPieces.remove(self)
                    tempPieces.append(temp)

                    if Cboard[i][j] != None:
                        Cboard[i][j].tempEaten = True

                    if not king.canBeEaten(king.x, king.y, tempBoard, tempPieces):
                        availables.append([i, j])

                    if Cboard[i][j] != None:
                        Cboard[i][j].tempEaten = False
                    
        return availables
    
    def diagonalAvailable(self, squares, Cboard):     
       if self.x > 0 and self.y > 0:
           currX = self.x-1
           currY = self.y-1

           curr = Cboard[currX][currY]       
           finished = False
               
           while(not finished and (currX > -1 and currY > -1) and (curr == None or (curr.side != self.side))):
               if curr != None and curr.side != self.side:
                   squares[currX][currY] = True
                   finished = True
               squares[currX][currY] = True
               currX -= 1
               currY -= 1
               if currX != -1 and currY != -1:
                   curr = Cboard[currX][currY]
                
                   
                
       if self.x < 7 and self.y > 0:
           currX = self.x+1
           currY = self.y-1
           
           curr = Cboard[currX][currY]       
           finished = False
               
           while(not finished and (currX < 8 and currY > -1) and (curr == None or (curr.side != self.side))):
               if curr != None and curr.side != self.side:
                   squares[currX][currY] = True
                   finished = True
               squares[currX][currY] = True
               currX += 1
               currY -= 1
               if currX != 8 and currY != -1:
                   curr = Cboard[currX][currY]
       
       
       
       if self.x < 7 and self.y < 7:
           currX = self.x+1
           currY = self.y+1
           
           curr = Cboard[currX][currY]       
           finished = False
               
           while(not finished and (currX < 8 and currY < 8) and (curr == None or (curr.side != self.side))):
               if curr != None and curr.side != self.side:
                   squares[currX][currY] = True
                   finished = True
               squares[currX][currY] = True
               currX += 1
               currY += 1
               if currX != 8 and currY != 8:
                   curr = Cboard[currX][currY]
       
       
       
       if self.x > 0 and self.y < 7:
           currX = self.x-1
           currY = self.y+1
           
           curr = Cboard[currX][currY]       
           finished = False
               
           while(not finished and (currX > -1 and currY < 8) and (curr == None or (curr.side != self.side))):
               if curr != None and curr.side != self.side:
                   squares[currX][currY] = True
                   finished = True
               squares[currX][currY] = True
               currX -= 1
               currY += 1
               if currX != -1 and currY != 8:
                   curr = Cboard[currX][currY]
                    
    def orthogonalAvailable(self, squares, Cboard): 
        if self.x != 0:
            currX = self.x-1
            currY = self.y
            curr = Cboard[currX][currY]
            finished = False
            while(currX != -1 and (curr == None or (curr.side != self.side)) and not finished):
                if curr != None and curr.side != self.side:
                    squares[currX][currY] = True
                    finished = True
                squares[currX][currY] = True
                currX -= 1
                if currX != -1:
                    curr = Cboard[currX][currY]
          
        if self.x != 7:
            currX = self.x+1
            currY = self.y
            curr = Cboard[currX][currY]
            finished = False
            while(currX != 8 and (curr == None or (curr.side != self.side)) and not finished):
                if curr != None and curr.side != self.side:
                    squares[currX][currY] = True
                    finished = True
                squares[currX][currY] = True
                currX += 1
                if currX != 8:
                    curr = Cboard[currX][currY]
                                   
        if self.y != 0:
            currX = self.x
            currY = self.y-1
            curr = Cboard[currX][currY]
            finished = False
            while(currY != -1 and (curr == None or (curr.side != self.side)) and not finished):
                curr = Cboard[currX][currY]
                if curr != None and curr.side != self.side:
                    squares[currX][currY] = True
                    finished = True
                squares[currX][currY] = True
                currY -= 1
                if currY != -1:
                    curr = Cboard[currX][currY]
                      
        if self.y != 7:
            currX = self.x
            currY = self.y+1
            curr = Cboard[currX][currY]
            finished = False
            while(currY != 8 and (curr == None or (curr.side != self.side)) and not finished):
                if curr != None and curr.side != self.side:
                    squares[currX][currY] = True
                    finished = True
                squares[currX][currY] = True
                currY += 1
                if currY != 8:
                    curr = Cboard[currX][currY]
        
    def canReach(self, Cboard, coordinate):
        orthogonal = self.canReachOrthogonal(Cboard, coordinate)
        if orthogonal:
            return True
        diagonal = self.canReachDiagonal(Cboard, coordinate)
        if diagonal:
            return True
        
        
    def canReachOrthogonal(self, Cboard, coordinate):
        
        cx = coordinate[0]
        cy = coordinate[1]
        
        diffx = abs(cx - self.x)
        diffy = abs(cy - self.y)
        
        if diffx != 0 and diffy != 0:
            return False
        
        if diffx != 0:
            if self.x > cx:
                currX = self.x-1
                currY = self.y
                curr = Cboard[currX][currY]
                while(curr == None and currX > -1 and currX != cx):
                    currX -= 1
                    if currX != -1:
                        curr = Cboard[currX][currY]
                if currX == cx and currY == cy:
                    return True
                
            if self.x < cx:
                currX = self.x+1
                currY = self.y
                curr = Cboard[currX][currY]
                while(curr == None and currX < 8 and currX != cx):
                    currX += 1
                    if currX != 8:
                        curr = Cboard[currX][currY]
                if currX == cx and currY == cy:
                    return True
        else:
            if self.y > cy:
                currX = self.x
                currY = self.y-1
                curr = Cboard[currX][currY]
                while(curr == None and currY > -1 and currY != cy):
                    currY -= 1
                    if currY != -1:
                        curr = Cboard[currX][currY]
                if currX == cx and currY == cy:
                    return True
                
            if self.y < cy:
                currX = self.x
                currY = self.y+1
                curr = Cboard[currX][currY]
                while(curr == None and currY < 8 and currY != cy):
                    currY += 1
                    if currY != 8:
                        curr = Cboard[currX][currY]
                if currX == cx and currY == cy:
                    return True
        return False

    def canReachDiagonal(self, Cboard, coordinate):
        cx = coordinate[0]
        cy = coordinate[1]
        
        if self.x != 0 and self.y != 0:
            currX = self.x-1
            currY = self.y-1
            
            curr = Cboard[currX][currY]       
                
            while(curr == None and currX > -1 and currY > -1 and currX != cx and currY != cy):
                currX -= 1
                currY -= 1
                if currX != -1 and currY != -1:
                    curr = Cboard[currX][currY]
            
            if currX == cx and currY == cy:
                return True
                    
                 
        if self.x != 7 and self.y != 0:
            currX = self.x+1
            currY = self.y-1
            
            curr = Cboard[currX][currY]       
                
            while(curr == None and currX < 8 and currY > -1 and currX != cx and currY != cy):
                currX += 1
                currY -= 1
                if currX != 8 and currY != -1:
                    curr = Cboard[currX][currY]
            
            if currX == cx and currY == cy:
                return True
        
        
        if self.x != 7 and self.y != 7:
            currX = self.x+1
            currY = self.y+1
            
            curr = Cboard[currX][currY]       
                
            while(curr == None and currX < 8 and currY < 8 and currX != cx and currY != cy):
                currX += 1
                currY += 1
                if currX != 8 and currY != 8:
                    curr = Cboard[currX][currY]
                
            if currX == cx and currY == cy:
                return True
        
        
        if self.x != 0 and self.y != 7:
            currX = self.x-1
            currY = self.y+1
            
            curr = Cboard[currX][currY]       
                
            while(curr == None and currX > -1 and currY < 8 and currX != cx and currY != cy):
                currX -= 1
                currY += 1
                if currX != -1 and currY != 8:
                    curr = Cboard[currX][currY]
            
            if currX == cx and currY == cy:
                return True
        
        return False
#################################################        
class king(piece):
    def __init__(self, side, x, y):
        piece.__init__(self, side, x, y)
        self.notMoved = True
        if side == 1:
            self.name = "bking"
        else:
            self.name = "wking"
        
    def move(self, mx, my):
        piece.move(self, mx, my)  
        self.notMoved = True
    
    def availableSquares(self, Cboard, pieces):
        squares = [[False for i in range(8)] for j in range(8)]
        availables = list()

        coordinates = list()
        
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    continue
                if self.x-1 + i >= 0 and self.y-1 + j >= 0 and self.x-1 + i <= 7 and self.y-1 + j <= 7 and (Cboard[self.x-1 + i][self.y-1 + j] == None or Cboard[self.x-1 + i][self.y-1 + j].side != self.side):
                    squares[self.x-1+i][self.y-1+j] = True
                    coordinates.append([self.x-1+i, self.y-1+j])
                
        for piece in pieces:
            if piece.available and piece.side != self.side:
                for coordinate in coordinates: 
                    tempBoard = cpy.deepcopy(Cboard)
                    tempBoard[self.x][self.y] = None
                    tempBoard[coordinate[0]][coordinate[1]] = self
                    reach = piece.canReach(tempBoard, coordinate)
                    if reach:
                        squares[coordinate[0]][coordinate[1]] = False

        for i in range(8):
            for j in range(8):
                if squares[i][j] == True:
                    availables.append([i, j])
        return availables
    
    def canReach(self, Cboard, coordinate):
        possibleList = list()
        
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    continue
                if self.x-1 + i >= 0 and self.y-1 + j >= 0 and self.x-1 + i <= 7 and self.y-1 + j <= 7 and (Cboard[self.x-1 + i][self.y-1 + j] == None or Cboard[self.x-1 + i][self.y-1 + j].side != self.side):
                    possibleList.append([self.x-1+i, self.y-1+j])
                    
        for i in possibleList:
            if coordinate == i:
                return True
            
        return False

    def canBeEaten(self, x, y, Cboard, pieces):
        for piece in pieces:
            if piece.available and not piece.tempEaten and piece.side != self.side:
                tempBoard = cpy.deepcopy(Cboard)
                tempBoard[self.x][self.y] = None
                tempBoard[x][y] = self
                reach = piece.canReach(tempBoard, (x, y))
                if reach:
                    return True
        return False
        
        
        