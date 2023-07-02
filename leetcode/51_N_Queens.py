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
