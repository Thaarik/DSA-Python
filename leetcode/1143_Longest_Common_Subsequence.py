"""
1143. Longest Common Subsequence
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
 

Constraints:

1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.

"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]
        for r in range(len(text1)-1, -1, -1):
            for c in range(len(text2)-1, -1, -1):
                if text1[r]==text2[c]:
                    dp[r][c]=1+dp[r+1][c+1]
                else:
                    dp[r][c]=max(dp[r+1][c],dp[r][c+1])
        return dp[0][0]
        

# Longest Common Subsequence
# Approach: Dynamic Programming
# Steps:
# 1. Create a 2D DP table where dp[i][j] = length of LCS of text1[i:] and text2[j:]
# 2. Fill the table bottom-up (from end to start of both strings)
# 3. For each position, if characters match, add 1 to the LCS of remaining substrings
# 4. If characters don't match, take the maximum LCS by either skipping a character from text1 or text2
#
# Example: text1 = "ace", text2 = "abcde"
#
# Initialize dp grid (rows = text1 + 1, cols = text2 + 1):
# [0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0]
#
# Fill dp grid (from bottom-right to top-left):
# - For r=2, c=4: text1[2]='e', text2[4]='e', match! dp[2][4] = 1 + dp[3][5] = 1
# - For r=1, c=2: text1[1]='c', text2[2]='c', match! dp[1][2] = 1 + dp[2][3] = 1
# - For r=0, c=0: text1[0]='a', text2[0]='a', match! dp[0][0] = 1 + dp[1][1] = 1 + 1 = 2
# - For cells with no match, take max(dp[r+1][c], dp[r][c+1])
#
# Final dp grid (after filling):
# [3, 2, 2, 1, 1, 0]
# [2, 2, 2, 1, 1, 0]
# [1, 1, 1, 1, 1, 0]
# [0, 0, 0, 0, 0, 0]
#
# Answer: 3 (the value at dp[0][0])
#
# The LCS is "ace"
#
# Intuition:
# - If the current characters match, we include them in our LCS and look for the LCS of remaining substrings
# - If they don't match, we have two options: skip the current character from text1 or text2
# - We take the maximum LCS from these two options
# - We work backwards from the end of both strings to build the LCS length at each position
# - dp[0][0] gives the LCS length for the entire strings
#
# Time: O(m*n) - we fill each cell in the dp table once
# Space: O(m*n) - we need to store the entire dp table


'''
Optimized with space:

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [0] * (n + 1)
        for r in range(m - 1, -1, -1):
            prev = 0
            for c in range(n - 1, -1, -1):
                temp = dp[c]
                if text1[r] == text2[c]:
                    dp[c] = 1 + prev
                else:
                    dp[c] = max(dp[c], dp[c + 1])
                prev = temp
        return dp[0]

# Longest Common Subsequence with space optimization    
# Approach: Dynamic Programming with Space Optimization
# Steps:# 1. Use a 1D DP array instead of a 2D table to save space
# 2. Iterate through the rows of text1 and update the DP array for each character in text2
# 3. Use a temporary variable to store the previous value needed for the current calculation
# 4. Return the first element of the DP array which contains the length of the longest common subsequence
              
'''
