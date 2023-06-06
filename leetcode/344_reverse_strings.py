# 344. Reverse String
# Easy

# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory

class Solution:
    def reverseString(self, s: List[str]) -> None:
        
        l = 0
        r = len(s)-1
        while l<r:
            s[l],s[r]=s[r],s[l]
            l+=1
            r-=1
        return s
        """
        Do not return anything, modify s in-place instead.
        """


        ''' Recursive Approach'''

    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def helper(s,start,end):
            if start>=end:
                return
            s[start],s[end]=s[end],s[start]
            helper(s,start+1,end-1)
        helper(s,0,len(s)-1)