'''
387. First Unique Character in a String
Easy

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1
 

Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.
'''

class Solution:
    def firstUniqChar(self, s: str) -> int:
        stringlist = list(s)
        stringCounter = Counter(s)
        for i in range(len(stringlist)):
            if stringlist[i] in stringCounter and stringCounter[stringlist[i]]==1:
                return i
        return -1

        

