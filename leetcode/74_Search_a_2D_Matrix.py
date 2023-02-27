'''
74. Search a 2D Matrix
Medium
11.5K
337
Companies
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # First Approach
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])-1,-1,-1):
        #         if target <= matrix[i][j]:
        #             start = 0
        #             end = j
        #             while start<=end:
        #                 middle = (start+end)//2
        #                 if matrix[i][middle]==target:
        #                     return True
        #                 elif matrix[i][middle]>target:
        #                     end=middle-1
        #                 else:
        #                     start = middle+1
        # return False

        #Second Approach
        #choose the correct row 
        top = 0
        bottom = len(matrix)-1
        
        while(top <= bottom):
            middle = (top+bottom)//2
            if (target>matrix[middle][-1]): #checks whether the target value is greater than the last value of choosen middle row
                top = middle+1
            elif (target<matrix[middle][0]): #checks whether the target value is less than the first value of choosen middle row
                bottom=middle-1
            else: #if the target value is not greater than the last value and not smaller than the first value of the chosen row, break
                break
        
        if (top > bottom) : return False

        #check whether that value exist in the choosen row
        left = 0
        right = len(matrix[0])-1
        while(left<=right):
            center = (left+right)//2
            if target < matrix[middle][center]:
                right=center-1
            elif target > matrix[middle][center]:
                left = center+1
            else:
                return True
        return False
