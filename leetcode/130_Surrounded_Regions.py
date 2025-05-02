"""
130. Surrounded Regions
Solved
Medium
Topics
Companies
You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.

 

Example 1:

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

Explanation:


In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

Example 2:

Input: board = [["X"]]

Output: [["X"]]

 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.
"""

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROW = len(board)
        COL= len(board[0])
        visited=set()
        def capture(r,c):
            if r<0 or c<0 or r>=ROW or c>=COL or board[r][c]!="O":
                return
            board[r][c]="T"
            capture(r+1,c)
            capture(r-1,c)
            capture(r,c+1)
            capture(r,c-1)
        
        for r in range(ROW):
            if board[r][0]=="O":
                capture(r,0)
            if board[r][COL-1]=="O":
                capture(r,COL-1)
        for c in range(COL):
            if board[0][c]=="O":
                capture(0,c)
            if board[ROW-1][c]=="O":
                capture(ROW-1,c)

        for r in range(ROW):
            for c in range(COL):
                if board[r][c]=="O":
                    board[r][c]="X"
                if board[r][c]=="T":
                    board[r][c]="O"


# Surrounded Regions
# Approach: DFS from Border "O"s
# Steps:
# 1. Mark all "O"s connected to the border/edge as "T" (temporary marker)
# 2. Convert remaining "O"s (which are surrounded) to "X"
# 3. Convert all "T"s back to "O"s
#
# Diagram for board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]:
#
# Initial board:
# [
#   ["X","X","X","X"],
#   ["X","O","O","X"],
#   ["X","X","O","X"],
#   ["X","O","X","X"]
# ]
#
# Step 1: Mark border-connected "O"s as "T"
# - Start DFS from each border cell
# - Bottom left (3,1) is "O", mark as "T" (using DFS)
#
# After marking border-connected "O"s:
# [
#   ["X","X","X","X"],
#   ["X","O","O","X"],
#   ["X","X","O","X"],
#   ["X","T","X","X"]  // Only this "O" is connected to border
# ]
#
# Step 2 & 3: Convert remaining "O"s to "X" and restore "T"s to "O"s
# 
# Final board:
# [
#   ["X","X","X","X"],
#   ["X","X","X","X"],
#   ["X","X","X","X"],
#   ["X","O","X","X"]
# ]
#
# Intuition:
# - "O"s are only captured if they are completely surrounded by "X"s
# - Any "O" connected to the border cannot be captured
# - Instead of checking each "O" cell to see if it's surrounded, we mark all border-connected "O"s
# - Any unmarked "O" must be surrounded and can be flipped to "X"
#
# Time: O(N×M) where N and M are dimensions of the board
#       - We potentially visit each cell during DFS
#
# Space: O(N×M) for the recursion stack in worst case
#       - When the board is filled with "O"s connected to the border
#
# Note: The code has an unused "visited" set - this is not needed as we use the board itself
# to track visited cells by changing "O" to "T"
       
