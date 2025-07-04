"""286. Walls And Gates - Explanation
Problem Link

Description
You are given a 
m
×
n
m×n 2D grid initialized with these three possible values:

-1 - A water cell that can not be traversed.
0 - A treasure chest.
INF - A land cell that can be traversed. We use the integer 2^31 - 1 = 2147483647 to represent INF.
Fill each land cell with the distance to its nearest treasure chest. If a land cell cannot reach a treasure chest than the value should remain INF.

Assume the grid can only be traversed up, down, left, or right.

Modify the grid in-place.

Example 1:

Input: [
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]

Output: [
  [3,-1,0,1],
  [2,2,1,-1],
  [1,-1,2,-1],
  [0,-1,3,4]
]
Example 2:

Input: [
  [0,-1],
  [2147483647,2147483647]
]

Output: [
  [0,-1],
  [1,2]
]
Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
grid[i][j] is one of {-1, 0, 2147483647}

Keyword arguments:
argument -- description
Return: return_description
"""
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW, COL = len(grid), len(grid[0])
        queue = [] 
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c]==0:
                    queue.append((r,c)) 
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        while queue:
            row, col = queue.pop(0)
            for dr, dc in directions:
                newRow = dr+row
                newCol = dc+col
                if 0<=newRow<ROW and 0<=newCol<COL and grid[newRow][newCol] == 2**31-1:
                    grid[newRow][newCol]=grid[row][col]+1
                    queue.append((newRow,newCol))