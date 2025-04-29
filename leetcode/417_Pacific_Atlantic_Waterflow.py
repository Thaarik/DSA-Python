'''
417. Pacific Atlantic Water Flow
Solved
Medium
Topics
Companies
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

 

Example 1:


Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean 
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean 
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean 
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean 
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean 
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
Example 2:

Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.
 

Constraints:

m == heights.length
n == heights[r].length
1 <= m, n <= 200
0 <= heights[r][c] <= 105
'''

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW = len(heights)
        COL = len(heights[0])
        pac, atl = set(), set()
        
        def dfs(r,c,visited,prevHeight):
            if (r,c) in visited or r<0 or c<0 or r>=ROW or c>=COL or heights[r][c]<prevHeight:
                return
            visited.add((r,c))
            dfs(r+1,c,visited,heights[r][c])
            dfs(r-1,c,visited,heights[r][c])
            dfs(r,c+1,visited,heights[r][c])
            dfs(r,c-1,visited,heights[r][c])

        for c in range(COL):
            dfs(0,c,pac,heights[0][c])
            dfs(ROW-1,c,atl, heights[ROW-1][c])

        for r in range(ROW):
            dfs(r,0,pac,heights[r][0])
            dfs(r,COL-1,atl, heights[r][COL-1])

        result=[]
        for r in range(ROW):
            for c in range(COL):
                if (r,c) in pac and (r,c) in atl:
                    result.append([r,c])
        return result
    
# Approach:
#         1. DFS
#         2. Create two sets for pacific and atlantic oceans
#         3. Create a dfs function to check the cells that can flow to the pacific and atlantic oceans
#         4. For each cell in the first row and last row, call the dfs function for pacific and atlantic oceans respectively
#         5. For each cell in the first column and last column, call the dfs function for pacific and atlantic oceans respectively
#         6. Finally, check which cells are in both pacific and atlantic oceans and return the result
#         7. The time complexity is O(m*n) where m is the number of rows and n is the number of columns
#         8. The space complexity is O(m*n) for the visited set
#         9. The overall time complexity is O(m*n) and space complexity is O(m*n)


# Steps:
# 1. Start DFS from each ocean edge (Pacific and Atlantic)
# 2. Water flows from low to high elevation, so we search from ocean inward
# 3. Mark cells reachable from each ocean in separate sets
# 4. Return cells that are reachable from both oceans
#
# Diagram for heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]:
#
# Pacific Ocean is on the top and left edges
# Atlantic Ocean is on the bottom and right edges
#
#     Pacific
#     ↓ ↓ ↓ ↓ ↓
#   → [1,2,2,3,5]
# P → [3,2,3,4,4] → A
# a → [2,4,5,3,1] → t
# c → [6,7,1,4,5] → l
# i → [5,1,1,2,4] → a
# f   ↑ ↑ ↑ ↑ ↑   n
# i   Atlantic    t
# c               i
#                 c
#
# DFS from Pacific Edges:
# - Start from top row: (0,0), (0,1), (0,2), (0,3), (0,4)
# - Start from left col: (1,0), (2,0), (3,0), (4,0)
#
# For example, starting DFS from (0,0):
# - Cell (0,0) = 1 is added to pac set
# - Check neighbors:
#   - (1,0) = 3 > 1, so water can flow from (1,0) to (0,0), add (1,0) to pac set
#   - (0,1) = 2 > 1, so water can flow from (0,1) to (0,0), add (0,1) to pac set
#
# Pacific reachable cells:
# [
#   [P,P,P,P,P],  // P = Pacific reachable
#   [P,P,P,P,P],
#   [P,P,P,P,_],
#   [P,P,_,P,P],
#   [P,_,_,_,_]
# ]
#
# DFS from Atlantic Edges:
# - Start from bottom row: (4,0), (4,1), (4,2), (4,3), (4,4)
# - Start from right col: (0,4), (1,4), (2,4), (3,4)
#
# Atlantic reachable cells:
# [
#   [_,_,_,_,A],  // A = Atlantic reachable
#   [_,_,_,A,A],
#   [_,A,A,A,A],
#   [A,A,_,A,A],
#   [A,A,A,A,A]
# ]
#
# Cells reachable by both oceans (intersection):
# [
#   [_,_,_,_,P&A],
#   [_,_,_,P&A,P&A],
#   [_,P&A,P&A,P&A,_],
#   [P&A,P&A,_,P&A,P&A],
#   [P&A,_,_,_,_]
# ]
#
# Result: [[0,4], [1,3], [1,4], [2,1], [2,2], [2,3], [3,0], [3,1], [3,3], [3,4], [4,0]]
#
# Time: O(N×M) where N and M are dimensions of the grid
#      - We visit each cell at most twice (once for each ocean)
#
# Space: O(N×M) for the recursion stack and visited sets
#
# Key insight: Instead of checking if water flows to both oceans from each cell (which would be O(N²M²)),
# we check which cells can receive water from both oceans (by reversing the flow direction)
