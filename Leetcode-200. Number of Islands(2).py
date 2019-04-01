def cleaning (i, j, grid, x, y):
    grid[i][j]=0
    #check right
    if (j<x-1) and (grid[i][j+1] == '1'):
        cleaning(i, j+1, grid, x, y)
    #check down
    if (i<y-1) and (grid[i+1][j] == '1'):
        cleaning(i+1, j, grid, x, y)
    #check left
    if (j>0) and (grid[i][j-1] == '1'):
        cleaning(i, j-1, grid, x, y)
    #check up
    if (i>0) and (grid[i-1][j] == '1'):
        cleaning(i-1, j, grid, x, y)
        

class Solution(object):  
    def numIslands(self, grid):
        count = 0
        y = len(grid)
        if y == 0:
            return 0
        x = len(grid[0])
        
        for i in range(y):
            for j in range(x):
                if grid[i][j] == '1':
                    count +=1 
                    cleaning(i, j, grid, x, y )     
        return count
        