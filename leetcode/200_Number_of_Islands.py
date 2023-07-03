"""
200. Number of Islands
Medium
20.3K
446
Companies
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """ Recursive approach """
        # count = 0
        # def dfs(grid, row,col):
        #     if (row<0 or row >= len(grid) or col <0 or col>=len(grid[0])): #Out of bound
        #         return
        #     if grid[row][col]=="1": #if you find on e in itself and neighbouring.
        #         grid[row][col]="-" # turn something else and move onto neighbouring grid
        #         dfs(grid,row-1,col)
        #         dfs(grid,row+1,col)
        #         dfs(grid,row,col-1)
        #         dfs(grid,row,col+1)

        # for row in range(len(grid)):
        #     for column in range(len(grid[row])):
        #         if grid[row][column]=="1":
        #             dfs(grid,row,column)
        #             count+=1
        # return count
        """ Iterative Approach: """
        def dfs(grid, row,col):
            stack=[]
            stack.append((row,col))
            while stack:
                row,col=stack.pop()
                grid[row][col]="-"
                if row >0 and grid[row-1][col]=="1":
                    stack.append((row-1,col))
                if row <len(grid)-1 and grid[row+1][col]=="1":
                    stack.append((row+1,col))
                if col >0 and grid[row][col-1]=="1":
                    stack.append((row,col-1))
                if col <len(grid[0])-1 and grid[row][col+1]=="1":
                    stack.append((row,col+1))

        count=0
        for row in range(len(grid)):
            for column in range(len(grid[row])):
                if grid[row][column]=="1":
                    dfs(grid,row,column)
                    count+=1
        return count        
"""
Approach:
If you find 1, increment count, make its neighbouring 1's (horizontal and vertical) into something else ('-') and move on. So that the function counts only those that are not neighbouring which appears to be 1 and not as '-'.
"""