'''
542. 01 Matrix
Medium
7.5K
342
Companies
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

 

Example 1:


Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]
Example 2:


Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
mat[i][j] is either 0 or 1.
There is at least one 0 in mat.
'''

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = collections.deque()
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col]==0:
                    queue.append((row,col)) # append all index of 0 value
                else:
                    mat[row][col]=math.inf # change values of 1 to infinity
        while queue:
            row,col=queue.popleft()
            for dir_row,dir_col in directions: # for every zero element, check its nearest neighbours
                new_row = row+dir_row
                new_col = col+dir_col
                if 0<=new_row<len(mat) and 0<=new_col<len(mat[0]) and mat[new_row][new_col]>mat[row][col]+1: # if the neighbour is inbound and contains infinity or some value greater than the chosen (popped queue) indexes
                    queue.append((new_row,new_col)) # append the neighbour index for further investigation of infinity (left out 1)
                    mat[new_row][new_col]=mat[row][col]+1 # change the neighbour value to chosen (popped queue) value + 1
        return mat

