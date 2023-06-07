'''
119. Pascal's Triangle II
Easy

Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]
 

Constraints:

0 <= rowIndex <= 33
 
 '''

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = []
        for i in range(rowIndex+1):
            row.append([])
            for j in range(i+1):
                if j==0 or j==i:
                    row[i].append(1) #if the indexes are 0th are '-1'th, then append 1
                else:
                    row[i].append(row[i-1][j-1]+row[i-1][j]) #if not then add the previous indexes value
        return row[-1] #last value
    

        '''recursive Approach'''
        # Base case: First row
        if rowIndex == 0:
            return [1]

        # Recursive case
        prev_row = self.getRow(rowIndex - 1)
        row = [1]  # First element is always 1

        for i in range(1, rowIndex):
            row.append(prev_row[i - 1] + prev_row[i])

        row.append(1)  # Last element is always 1

        return row