# Search word in Word matrix
# Problem

'''
Define Board
Search word
    row and col - length of board and length of first column
    Path to keep track of paths
'''

class myWordmatrix:
    def __init__(self, board):
        self.board = board

    def exist(self, word):
        rows, cols = len(self.board), len(self.board[0])
        path = set()
        
        def dfs(r, c, i):
            if i == len(word):
                return True
            if r < 0 or r >= rows or c <  0 or c >= cols or self.board[r][c] != word[i] or (r,c) in path:
                return False

            path.add((r,c))
            res = dfs(r + 1, c, i+1) or dfs(r - 1, c, i+1) or dfs(r, c + 1, i+1) or dfs(r , c - 1, i + 1)
            path.remove((r,c))
            return res

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0): return True
        
        return False

board = [["A","S","C","E"],["S","A","N","D"],["A","P","E","E"]]
word = "PRADNYA"
myObj = myWordmatrix(board)
print(myObj.exist(word))