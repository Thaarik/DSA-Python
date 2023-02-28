'''
36. Valid Sudoku
Medium


Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
 

Example 1:


Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
'''

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #checks whether the number is unique in every rows cells
        def notInRow(board,row):
            checkNum = set()
            for i in range(0,9):
                if board[row][i] in checkNum:
                    return False
                if board[row][i]!=".":
                    checkNum.add(board[row][i])
            return True
        
        #checks whether the number is unique in every column cells
        def notInColumn(board,column):
            checkNum = set()
            for i in range(0,9):
                if board[i][column] in checkNum:
                    return False
                if board[i][column]!=".":
                    checkNum.add(board[i][column])
            return True

        #checks whether the number is unique in every 3x3 matrix cells
        def notIn3x3Matrix(board,row,col):
            checkNum = set()
            for r in range(0,3):
                for c in range(0,3):
                    currentElement = board[row+r][col+c]

                    if currentElement in checkNum:
                        return False
                    if currentElement != ".":
                        checkNum.add(currentElement)
            return True

        # if anyone above function is false, return false, else return true
        for row in range(len(board)):
            for col in range(len(board[0])):
                if (notInRow(board,row) and 
                notInColumn(board,col) and 
                notIn3x3Matrix(board,row-row%3,col-col%3)) != True:
                    return False
        return True

        ''' ANOTHER APPROACH
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for c in range(9):
            for r in range(9):
                number = board[r][c]
                if number == ".":
                    continue
                if number in cols[c] or number in rows[r] or number in squares[(r // 3, c // 3)]:
                    return False
                cols[c].add(number)
                rows[r].add(number)
                squares[(r // 3, c // 3)].add(number)

        return True
         '''

            

