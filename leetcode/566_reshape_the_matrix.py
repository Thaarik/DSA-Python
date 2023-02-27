'''
566. Reshape the Matrix
Easy

In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

 

Example 1:


Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]
Example 2:


Input: mat = [[1,2],[3,4]], r = 2, c = 4
Output: [[1,2],[3,4]]
'''

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        res = [[0 for i in range(c)] for j in range(r)]
        row = 0
        column = 0
        # if the product of r*c is not equal to the given matrix's row and column product, return the matrix itself
        if (len(mat)*len(mat[0])!=r*c): 
            return mat
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                print(i,j)
                print(row,column)
                res[row][column]=mat[i][j]
                column+=1
                if column==c:
                    row+=1
                    column=0

        return res