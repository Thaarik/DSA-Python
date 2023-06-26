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
