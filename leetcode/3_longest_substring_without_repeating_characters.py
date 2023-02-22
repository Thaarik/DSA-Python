# 3. Longest Substring Without Repeating Characters
# Medium


# Given a string s, find the length of the longest 
# substring
#  without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        # using set to remove the duplicates.
        charset = set()
        left = 0
        res = 0
        for right in range(n):
            while s[right] in charset:
                charset.remove(s[left])
                left+=1
            charset.add(s[right])
            res = max(res,len(charset))
        return res

