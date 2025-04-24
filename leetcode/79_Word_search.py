'''
79. Word Search
Medium
13.6K
551
Companies
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 

Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
 

Follow up: Could you use search pruning to make your solution faster with a larger board?
'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW = len(board)
        COL = len(board[0])
        path = set()

        def backtrack(row, col,i): # i- ith index of each character in target word
            if i == len(word): # if ith index of the character in thw target word reaches it's end i.e., equal to the length of the target word
                return True
            if(row<0 or col <0 or row>=ROW or col>=COL or # out of bound condition
            board[row][col]!=word[i] or # when the target word[i] not equal to the current board[i]
            (row,col) in path): # when we come across the used path
                return False
            path.add((row,col))
            # check in all directions and store when we it satisfies the above condition and returns true
            res = (backtrack(row+1,col,i+1) or 
                   backtrack(row-1,col,i+1) or 
                   backtrack(row,col+1,i+1) or 
                   backtrack(row,col-1,i+1))
            path.remove((row,col))
            return res

        for r in range(ROW):
            for c in range(COL):
                if backtrack(r,c,0):
                    return True
        return False 

#TC : O(N * M * 4 ^ (backtrack))

# Word Search
# Approach: Backtracking/DFS
# Steps:
# 1. For each cell in the board, try starting the word search from there
# 2. Use backtracking to explore adjacent cells (up, down, left, right)
# 3. Keep track of visited cells using a set to avoid reusing same cell
# 4. Stop when either the word is found or all possibilities are exhausted
#
# Diagram of recursive calls for board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE":
#
# Starting from each cell, but illustration shows only successful path:
#
# Start at board[1][0] = "S"  (path = {(1,0)})
#   |
#   |-- backtrack(1,0,0) - Checking 'S' matches word[0]='S' ✓
#       |
#       |-- backtrack(2,0,1) - Down - 'A' ≠ word[1]='E' ✗
#       |
#       |-- backtrack(0,0,1) - Up - 'A' ≠ word[1]='E' ✗
#       |
#       |-- backtrack(1,1,1) - Right - 'F' ≠ word[1]='E' ✗
#       |
#       |-- backtrack(1,-1,1) - Left - Out of bounds ✗
#
# Start at board[2][2] = "E"
#   |
#   |-- backtrack(2,2,1) - Checking 'E' matches word[1]='E' ✓ (path = {(1,0), (2,2)})
#       |
#       |-- backtrack(3,2,2) - Down - Out of bounds ✗
#       |
#       |-- backtrack(1,2,2) - Up - 'C' ≠ word[2]='E' ✗
#       |
#       |-- backtrack(2,3,2) - Right - 'E' matches word[2]='E' ✓ (path = {(1,0), (2,2), (2,3)})
#           |
#           |-- backtrack(3,3,3) - Index 3 = len(word) ✓ Found complete word!
#           |   Return True
#           |
#           |-- Remove (2,3) from path
#       |
#       |-- Remove (2,2) from path
#   |
#   |-- Remove (1,0) from path
#
# Visual representation of the successful path on the board:
#
# [["A","B","C","E"],
#  ["S","F","C","S"],  -> Start at S, then move to E, then to E
#  ["A","D","E","E"]]
#               ^
#               |
#               End here
#
# Time: O(N * M * 4^L) where N,M are board dimensions, L is word length, 4 is for four directions
# Space: O(L) for recursion stack depth and path set
#
# Optimization tip: We could check if all required letters exist in the board before starting,
# or sort the word locations by frequency to start with rare letters first.

