'''
22. Generate Parentheses
Medium
18.1K
735
Companies
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8
'''

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # add open bracket only if openN < n
        # add closed bracket only if closedN < n and closedN < openN
        # Base case -> openN == closedN == n



        def backtracking(res, stack, openN,closedN):
            if openN==closedN==n:
                res.append(stack)
            if openN < n:
                backtracking(res,stack+'(',openN+1,closedN)
            if closedN <n and closedN < openN:
                backtracking(res,stack+')',openN,closedN+1)
        res = []
        backtracking(res,'',0,0)
        return res
