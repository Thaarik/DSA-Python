"""
51. N-Queens
Hard
10.5K
229
Companies
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

 

Example 1:


Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
Example 2:

Input: n = 1
Output: [["Q"]]
 

Constraints:

1 <= n <= 9
"""

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        column = set()
        posDiag = set() # (row+column)
        negDiag = set() # (row-column)
        result=[]
        board=[["."]*n for i in range(n)]# if n=4 -> [['.', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.']]
        def backtrack(row):
            if row==n:
                boardcopy = ["".join(r) for r in board] # ['.Q..', '...Q', 'Q...', '..Q.']
                print(boardcopy)
                result.append(boardcopy)
                return
            for col in range(n):
                if col in column or (row+col) in posDiag or (row-col) in negDiag:
                    continue
                column.add(col)
                posDiag.add(row+col)
                negDiag.add(row-col)
                board[row][col]="Q"
                backtrack(row+1)
                column.remove(col)
                posDiag.remove(row+col)
                negDiag.remove(row-col)
                board[row][col]="."
        backtrack(0)
        return result

"""        Approach:
        1. Backtracking
        2. out main goal is to fill the column set( ) with column inex where queen has been set, then add the queens movement diagonals. positive diagonals -> row+col, negative diagonal -> row-col
        3. if we choose a column, and that column does not contain in above sets, then we can add the queen. otherwise ignore."""

# N-Queens Problem
# Approach: Backtracking with Sets for O(1) Constraint Checking
# Steps:
# 1. Place queens row by row, trying each column position
# 2. Track occupied columns and diagonals using sets for O(1) lookup
# 3. Use backtracking to explore all possible board configurations
# 4. When all N queens are placed, add the solution to result
#
# Diagram of recursive calls for n=4:
#
# backtrack(0) - Starting with empty board
#  |
#  |-- Try Q at (0,0)
#  |   |-- COL={0}, posDiag={0}, negDiag={0}
#  |   |-- Board: ["Q...", "....", "....", "...."]
#  |   |
#  |   |-- backtrack(1) - Try row 1
#  |       |
#  |       |-- Try Q at (1,0) ✗ Column conflict
#  |       |-- Try Q at (1,1) ✗ Diagonal conflict
#  |       |-- Try Q at (1,2) 
#  |       |   |-- COL={0,2}, posDiag={0,3}, negDiag={0,-1}
#  |       |   |-- Board: ["Q...", "..Q.", "....", "...."]
#  |       |   |
#  |       |   |-- backtrack(2) - Try row 2
#  |       |       |-- All positions conflict ✗
#  |       |   |
#  |       |   |-- Backtrack: Remove Q from (1,2)
#  |       |
#  |       |-- Try Q at (1,3)
#  |           |-- COL={0,3}, posDiag={0,4}, negDiag={0,-2}
#  |           |-- Board: ["Q...", "...Q", "....", "...."]
#  |           |
#  |           |-- backtrack(2) - Try row 2
#  |               |
#  |               |-- Try Q at (2,1)
#  |                   |-- COL={0,3,1}, posDiag={0,4,3}, negDiag={0,-2,1}
#  |                   |-- Board: ["Q...", "...Q", ".Q..", "...."]
#  |                   |
#  |                   |-- backtrack(3) - Try row 3
#  |                       |
#  |                       |-- All positions conflict ✗
#  |
#  |-- Try Q at (0,1)
#  |   |-- COL={1}, posDiag={1}, negDiag={-1}
#  |   |-- Board: [".Q..", "....", "....", "...."]
#  |   |
#  |   |-- backtrack(1) - Try row 1
#  |       |
#  |       |-- Try Q at (1,3)
#  |           |-- COL={1,3}, posDiag={1,4}, negDiag={-1,-2}
#  |           |-- Board: [".Q..", "...Q", "....", "...."]
#  |           |
#  |           |-- backtrack(2) - Try row 2
#  |               |
#  |               |-- Try Q at (2,0)
#  |                   |-- COL={1,3,0}, posDiag={1,4,2}, negDiag={-1,-2,2}
#  |                   |-- Board: [".Q..", "...Q", "Q...", "...."]
#  |                   |
#  |                   |-- backtrack(3) - Try row 3
#  |                       |
#  |                       |-- Try Q at (3,2)
#  |                           |-- COL={1,3,0,2}, posDiag={1,4,2,5}, negDiag={-1,-2,2,1}
#  |                           |-- Board: [".Q..", "...Q", "Q...", "..Q."]
#  |                           |
#  |                           |-- backtrack(4) - All queens placed ✓
#  |                           |-- Add solution: [".Q..","...Q","Q...","..Q."]
#
# Solutions for n=4:
# [
#   [".Q..",  // Solution 1
#    "...Q",
#    "Q...",
#    "..Q."],
# 
#   ["..Q.",  // Solution 2
#    "Q...",
#    "...Q",
#    ".Q.."]
# ]
#
# Time: O(N!) - For each row, we have at most N choices (usually fewer due to constraints)
# Space: O(N) - For tracking columns and diagonals plus the recursion stack
#
# Key insights:
# 1. We track diagonals using row+col (positive diagonal) and row-col (negative diagonal)
# 2. We only need to check upward conflicts since we're filling the board top to bottom
# 3. Each row must have exactly one queen (enforced by our row-by-row placement)

