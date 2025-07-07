'''
62. Unique Paths
Solved
Medium
Topics
premium lock icon
Companies
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

 

Example 1:


Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
 
'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for _ in range(m)]
        dp[0][0]=1
        for i in range(m):
            for j in range(n):
                if i>0 and j>0:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
                elif i>0:
                    dp[i][j]=dp[i-1][j]
                elif j>0:
                    dp[i][j]=dp[i][j-1]
        return dp[m-1][n-1]
        

        # Unique Paths
# Approach: Dynamic Programming
# Steps:
# 1. Create a 2D DP table where dp[i][j] = number of ways to reach cell (i,j)
# 2. Set the starting point dp[0][0] = 1 (only one way to start)
# 3. For each cell, the number of ways to reach it equals the sum of ways to reach the cell above and the cell to the left
# 4. Return the value at the bottom-right cell
#
# Example: m=3, n=3
#
# Initialize dp grid:
# [1, 0, 0]
# [0, 0, 0]
# [0, 0, 0]
#
# Fill dp grid (cell by cell):
# dp[0][1] = dp[0][0] = 1
# dp[1][0] = dp[0][0] = 1
# dp[1][1] = dp[0][1] + dp[1][0] = 1 + 1 = 2
# dp[0][2] = dp[0][1] = 1
# dp[1][2] = dp[0][2] + dp[1][1] = 1 + 2 = 3
# dp[2][0] = dp[1][0] = 1
# dp[2][1] = dp[1][1] + dp[2][0] = 2 + 1 = 3
# dp[2][2] = dp[1][2] + dp[2][1] = 3 + 3 = 6
#
# Final dp grid:
# [1, 1, 1]
# [1, 2, 3]
# [1, 3, 6]
#
# Answer: 6 (the value at dp[2][2])
#
# Intuition:
# - A robot can only move right or down
# - To reach any cell (i,j), the robot must come from either:
#   * The cell above (i-1,j) by moving down
#   * The cell to the left (i,j-1) by moving right
# - The total number of paths is the sum of paths from these two sources
# - Edge cases: cells in the first row or first column can only be reached in one way
#
# Time: O(m*n) - we need to fill every cell in the dp table
# Space: O(m*n) - we need to store the entire dp table
#
# Note: This problem has a combinatorial solution as well: C(m+n-2, m-1) or C(m+n-2, n-1)
