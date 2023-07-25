'''
1254. Number of Closed Islands
Medium
4.2K
144
Companies
Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.

 

Example 1:



Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by water (group of 1s).
Example 2:



Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1
Example 3:

Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2
 

Constraints:

1 <= grid.length, grid[0].length <= 100
0 <= grid[i][j] <=1
'''

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        count=0
        def dfs(row,col,grid,visited):
            if row<0 or row>=len(grid) or col<0 or col>=len(grid[0]) :
                return 0 #False because they are out of bound
            if grid[row][col]==1 or (row,col) in visited:
                return 1 # true because they are closed island or 0 already visited
            visited.add((row,col))
            return min(dfs(row-1,col,grid,visited),dfs(row+1,col,grid,visited),dfs(row,col-1,grid,visited),dfs(row,col+1,grid,visited)) # for every dfs call, if there exists any out of bound (0) then it returns that and oes not count as closed island. If all dfs calls returns 1, then it is a closed island
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==0 and (r,c) not in visited:
                    count+=dfs(r,c,grid,visited)

        return count