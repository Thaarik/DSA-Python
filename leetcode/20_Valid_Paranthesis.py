'''
20. Valid Parentheses
Easy

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'
'''

class Solution:
    def isValid(self, s: str) -> bool:
        
        ''' Approach 1'''
        #s1 = []
        # slist = list(s)
        # for i in range(0,len(slist)):
        #     if slist[i]=="(" or slist[i]=="{" or slist[i]=="[":
        #         s1.append(slist[i])
        #     else:
        #         if s1:
        #             if (s1[-1]=="(" and slist[i]==")") or (s1[-1]=="{" and slist[i]=="}")  or (s1[-1]=="[" and slist[i]=="]"):
        #                 s1.pop()
        #             else:
        #                 return False

        #         else:
        #             return False

        # if s1:
        #     return False
        # return True

        ''' Approach 2'''
        s1 = []
        smap = {")":"(","}":"{","]":"["}
        for i in s:
            #if i == ) or } or ]
            if i in smap:
                if s1 and smap[i]==s1[-1]:
                    s1.pop()
                else:
                    return False
            # if i = ( or { or [
            else:
                s1.append(i)
        if s1:
            return False
        return True

                 