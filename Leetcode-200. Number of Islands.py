def cleaning (i, grid, x, y):
    grid[i/x][i%x]=0
    #check right
    if (i%x != x-1) and (grid[i/x][i%x+1] == '1'):
        cleaning(i+1, grid, x, y)
    #check down
    if (i/x != y-1) and (grid[i/x+1][i%x] == '1'):
        cleaning (i+x, grid, x, y)
    #check left
    if (i%x != 0) and (grid[i/x][i%x-1] == '1'):
        cleaning(i-1, grid, x, y)
    #check up
    if (i/x != 0) and (grid[i/x-1][i%x] == '1'):
        cleaning (i-x, grid, x, y)
        

class Solution(object):  
    def numIslands(self, grid):
        count = 0
        y = len(grid)
        if y == 0:
            return 0
        x = len(grid[0])
        
        for i in range(x*y):
            if grid[i/x][i%x] == '1':
                count +=1 
                cleaning(i, grid, x, y )            
        return count
        
            