def circle(m, n, matrix, ans):
    x, y =0, 0
# Go Right
    while (matrix) and (x<m):
        ans.append(matrix[0][x])
        x += 1
    if(matrix): matrix.pop(0)
    x, n = x-2 ,n-1
# Go Down
    while (matrix) and (y<n) and (matrix[y]) :
        ans.append(matrix[y].pop())
        y += 1
    y, m = y-2, m-1
# Go Left
    while (matrix) and (x >= 0):
        ans.append(matrix[-1][x])
        x -= 1 
    if(matrix): matrix.pop()
    n -= 1
# Go Up
    while (matrix) and (matrix[0]) and (y >= 0):
        ans.append(matrix[y].pop(0))
        y = y-1
    m -= 1
    if matrix:
        return circle(m, n, matrix, ans)
    else:
        return ans
    
    
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        n = len(matrix)
        if n == 0:
            return []
        m = len(matrix[0])
        ans = []
        return circle(m, n, matrix, ans)
        