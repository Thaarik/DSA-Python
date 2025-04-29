"""
994. Rotting Oranges
Medium
10.9K
350
Companies
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

Example 1:


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.
"""
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        freshorangecount = 0
        minutes = 0
        row = len(grid)
        col = len(grid[0])
        # find the number of freshoranges and append the location of rotten oranges
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==1:
                    freshorangecount+=1
                if grid[r][c]==2:
                    q.append([r,c]) # so q has only  the coordinates of rotten oranges
        # direction coordinates to check the bounds in the grid while traversing
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        #do bfs
        while q and freshorangecount > 0:
            for i in range(len(q)): # for every rotten oranges
                row,col = q.popleft() # take the location of the rotten oranges
                # check the rotten orange's horizontal and vertical neighbouring oranges. if it isnot 1, ignore(continue). If 1, turn to 2 (rotten)
                for dr,dc in directions:
                    r = dr+row
                    c = dc+col
                    if r<0 or r>=len(grid) or c<0 or c>=len(grid[0]) or grid[r][c]!=1: #if it out of bound or not 1, continue
                        continue
                    grid[r][c]=2 # turn fresh orange(1) into rotten orange (2)
                    q.append([r,c]) # append its location in q
                    freshorangecount-=1 # fresh orange count decreaes
            minutes+=1 # update minutes

        if freshorangecount >0:
            return -1
        return minutes
    
    # Approach:

# Rotting Oranges
# Approach: BFS (Breadth-First Search) with Queue
# Steps:
# 1. Count fresh oranges and identify initial rotten oranges
# 2. Use BFS to simulate the rotting process minute by minute
# 3. In each minute, rot all fresh oranges adjacent to currently rotten ones
# 4. Continue until no more oranges can rot or all are rotten
#
# Diagram for grid = [[2,1,1],[1,1,0],[0,1,1]]:
#
# Initial state (minute 0):
# [
#   [2, 1, 1],  // 2 = rotten orange, 1 = fresh orange, 0 = empty
#   [1, 1, 0],
#   [0, 1, 1]
# ]
# Queue: [(0,0)]  // Position of initial rotten orange
# Fresh oranges: 6
#
# Minute 1:
# - Pop (0,0), check neighbors: (0,1) and (1,0) become rotten
# [
#   [2, 2, 1],  // Orange at (0,1) rots
#   [2, 1, 0],  // Orange at (1,0) rots
#   [0, 1, 1]
# ]
# Queue: [(0,1), (1,0)]  // New rotten oranges
# Fresh oranges: 4
#
# Minute 2:
# - Pop (0,1), check neighbors: (0,2) becomes rotten
# - Pop (1,0), check neighbors: (1,1) becomes rotten
# [
#   [2, 2, 2],  // Orange at (0,2) rots
#   [2, 2, 0],  // Orange at (1,1) rots
#   [0, 1, 1]
# ]
# Queue: [(0,2), (1,1)]  // New rotten oranges
# Fresh oranges: 2
#
# Minute 3:
# - Pop (0,2), no new rotten oranges
# - Pop (1,1), check neighbors: (2,1) becomes rotten
# [
#   [2, 2, 2],
#   [2, 2, 0],
#   [0, 2, 1]   // Orange at (2,1) rots
# ]
# Queue: [(2,1)]  // New rotten oranges
# Fresh oranges: 1
#
# Minute 4:
# - Pop (2,1), check neighbors: (2,2) becomes rotten
# [
#   [2, 2, 2],
#   [2, 2, 0],
#   [0, 2, 2]   // Orange at (2,2) rots
# ]
# Queue: [(2,2)]  // New rotten oranges
# Fresh oranges: 0
#
# Minute 4 ends, all oranges are rotten, return 4
#
# Time: O(N×M) where N and M are dimensions of the grid
#       - We visit each cell at most once
#
# Space: O(N×M) for the queue in worst case
#       - When all oranges are rotten and added to queue
#
# Key insight: Level-by-level BFS perfectly simulates the "minute-by-minute" rotting process

                    