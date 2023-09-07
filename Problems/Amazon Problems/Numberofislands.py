# Problem
# Given an m x n 2D binary grid grid which represents a map of '1's (land) 
# and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by 
# connecting adjacent lands horizontally or vertically. 
# You may assume all four edges of the grid are all surrounded by water.

'''
Start when you find an island +1 
Recursovely Call DFS until you mark all islands around it as 0 and then 
continue to find new island +1 and repeat untill all elements are visited
'''

def numIslands(grid):
        # Get rows and columns. 
        # Loop through row and columns to find 1 - increament island
        # Go DFS to find 1's around it and arount them - replace with 0 
        nr = len(grid)  # rows
        if(not nr):return 0
        nc = len(grid[0]) # cols
        
        num_islands = 0

        def dfs(grid ,row ,col):
        
            r = len(grid)
            c = len(grid[0])

            grid[row][col] = '0'
        
            if row-1>=0 and grid[row-1][col] == '1':
                dfs(grid, row-1, col)
            
            if row+1<r and grid[row+1][col] == '1':
                dfs(grid, row+1, col)
        
            if col-1>=0 and grid[row][col-1] == '1':
                dfs(grid, row, col-1)
        
            if col+1<c and grid[row][col+1] == '1':
                dfs(grid, row, col+1)

        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == '1':
                    num_islands += 1
                    dfs(grid,i,j)
        
        return num_islands


grid = [
  ["1","1","0","0","1"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

print(numIslands(grid))