'''
64. Minimum Path Sum
Medium
11.3K
145
Companies
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example 1:

Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 200
'''
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        for r in range(row):
            for c in range(col):
                if r==0 and c==0: # starting point
                    continue
                elif r==0: # when we reach the first row, we could only move horizontally
                    grid[r][c]=grid[r][c]+grid[r][c-1]
                elif c==0: # when we reach the first row, we could only move horizontally
                    grid[r][c]=grid[r][c]+grid[r-1][c]
                else: #when we are in between, move towards the nearest neighbour that has minimum calculated value
                    grid[r][c]=grid[r][c]+min(grid[r-1][c],grid[r][c-1])
        return grid[row-1][col-1] # the last element of the 2D array has the minimum distance calculated value
#So we are calculating and storing the minimum distant value in each cell starting from grid[0][0] and returning the end element value grid[len(row)-1][len(grid[0])-1]
