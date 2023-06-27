'''
784. Letter Case Permutation
Medium
4.4K
154
Companies
Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. Return the output in any order.

 

Example 1:

Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]
Example 2:

Input: s = "3z4"
Output: ["3z4","3Z4"]
 

Constraints:

1 <= s.length <= 12
s consists of lowercase English letters, uppercase English letters, and digits.
'''

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:

        #backtracking
        current = ""
        result = []
        def backtrack(s,current,index):
            # print(f'result: {result} current: {current}') #check this for better result
            if len(current)==len(s):
                return result.append(current)
            
            if s[index].isalpha():
                backtrack(s,current+s[index].lower(),index+1) 
                backtrack(s,current+s[index].upper(),index+1)
            else:
                backtrack(s,current+s[index],index+1)

        backtrack(s,current,0)
        return result

        #iterative
        # result = ['']

        # for i in s:
        #     current=[]
        #     for r in result:
        #         if i.isalpha():               
        #             current.append(r + i.lower())
        #             current.append(r + i.upper())
        #         else:
        #             current.append(r + i)
        #     print(current) # check this for better understanding on how iterative approach works
        #     result = current
        # return result