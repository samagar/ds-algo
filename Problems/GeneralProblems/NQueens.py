# Problem
# Place N Queens on chess board such that they are safe

'''
Algorithm



'''
from operator import truediv


class NQueens:
    def __init__(self, n):
        self.n = n
        self.board = [[0 for i in range(self.n)] for j in range(self.n)]

    def printQueens(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.board[i][j] == 1:
                    print("Q", end =" ")
                else:
                    print("-", end=" ")
            print("\n")

    def isPlaceSafe(self,row,col):
        # Horizontal columns check
        for i in range(self.n):
            if self.board[row][i] == 1: return False
        
        # Diagoal Check - Top Left to bottom right
        # No checking for + of coll index as thats latest queen position and nothing after that.
        j = col
        for i in range(row,-1,-1):
            if i<0: break
            if self.board[i][j] == 1: return False
            j -= 1

        # Diagoal Check - bottom right
        j = col
        for i in range(row,self.n):
            if i<0: break
            if self.board[i][j] == 1: return False
            j -= 1

        return True

    # Solve for position of Queen
    def solve(self, colindex):
        if colindex == self.n:
            return True
        
        for rowindex in range(self.n):
            if self.isPlaceSafe(rowindex,colindex):
                self.board[rowindex][colindex] = 1
                if self.solve(colindex+1):
                    return True
                self.board[rowindex][colindex] = 0

        return False

    def queenSolution(self):
        if self.solve(0):
            self.printQueens()
        else:
            print("No Solution")

queenObj = NQueens(4)
queenObj.queenSolution()
