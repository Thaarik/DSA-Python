'''
695. Max Area of Island
Medium

You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

 

Example 1:


Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.
'''

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if grid == None:
            return grid

        maximumArea = 0
        visited = set()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                maximumArea = max(maximumArea,self.areaOfIsland(grid,r,c,visited))
        return maximumArea
    
    def areaOfIsland(self,grid,r,c,visited):
        #if the rows and columns are out of bound or grid value is zero or the rows and columns of a grid containing one is already visited
        if r<0 or r>=len(grid) or c<0 or c>=len(grid[0]) or grid[r][c]==0 or (r,c) in visited:
            return 0
        #if it is one and it is not visited
        visited.add((r,c))
        
        return (1 + 
        self.areaOfIsland(grid,r-1,c,visited)+ 
        self.areaOfIsland(grid,r+1,c,visited)+ 
        self.areaOfIsland(grid,r,c-1,visited)+ 
        self.areaOfIsland(grid,r,c+1,visited))