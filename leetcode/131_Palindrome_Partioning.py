'''
131. Palindrome Partitioning
Solved
Medium
Topics
Companies
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
 

Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.
'''

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # Palindrome function
        def isPalindrome(str):
            if len(str)==0:
                return False
            l,r=0,len(str)-1
            while l<r:
                if str[l]!=str[r]:
                    return False
                l+=1
                r-=1
            return True
        
        res = []
        subset=[]
        # Backtracking function to find all palindrome partitions
        def backtrack(startIndex):
            if len(s)==startIndex:
                res.append(subset[:])
                return
            for i in range(startIndex,len(s)):
                endIndex = i+1 # for substring
                if isPalindrome(s[startIndex:endIndex]):
                    subset.append(s[startIndex:endIndex])
                    backtrack(i+1)
                    subset.pop()
        backtrack(0)
        return res
    
# Partition - Palindrome Partitioning (For input "aab")
# Approach: Backtracking with Palindrome Check
# Steps:
# 1. Use backtracking to find all valid partitions where each substring is a palindrome
# 2. For each position, try all possible substrings starting from that position
# 3. If substring is palindrome, include it and recursively process remaining string
# 4. Backtrack to explore all possibilities
#
# Diagram of recursive calls for "aab":
#
# backtrack(0) - Start with empty subset[]
#   |
#   |-- Check "a" (0:1) ✓ palindrome
#   |   |-- Add "a" to subset → subset=["a"]
#   |   |-- backtrack(1) - Process remaining "ab"
#   |   |   |
#   |   |   |-- Check "a" (1:2) ✓ palindrome
#   |   |   |   |-- Add "a" to subset → subset=["a","a"]
#   |   |   |   |-- backtrack(2) - Process remaining "b"
#   |   |   |   |   |
#   |   |   |   |   |-- Check "b" (2:3) ✓ palindrome
#   |   |   |   |   |   |-- Add "b" to subset → subset=["a","a","b"]
#   |   |   |   |   |   |-- backtrack(3) - Reached end, add to result ✓
#   |   |   |   |   |   |   Result: [["a","a","b"]]
#   |   |   |   |   |   |-- Remove "b" → subset=["a","a"]
#   |   |   |   |
#   |   |   |   |-- Remove "a" → subset=["a"]
#   |   |   |
#   |   |   |-- Check "ab" (1:3) ✗ not palindrome
#   |   |
#   |   |-- Remove "a" → subset=[]
#   |
#   |-- Check "aa" (0:2) ✓ palindrome
#   |   |-- Add "aa" to subset → subset=["aa"]
#   |   |-- backtrack(2) - Process remaining "b"
#   |   |   |
#   |   |   |-- Check "b" (2:3) ✓ palindrome
#   |   |   |   |-- Add "b" to subset → subset=["aa","b"]
#   |   |   |   |-- backtrack(3) - Reached end, add to result ✓
#   |   |   |   |   Result: [["a","a","b"], ["aa","b"]]
#   |   |   |   |-- Remove "b" → subset=["aa"]
#   |   |
#   |   |-- Remove "aa" → subset=[]
#   |
#   |-- Check "aab" (0:3) ✗ not palindrome
#
# Final result: [["a","a","b"], ["aa","b"]]
#
# Time: O(N * 2^N) - In worst case, we have 2^N possible partitions and each requires O(N) to check palindrome
# Space: O(N) - For recursion stack and current subset
