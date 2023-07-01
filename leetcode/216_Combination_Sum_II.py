"""
216. Combination Sum III
Medium
5.1K
97
Companies
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

 

Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.
Example 3:

Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations.
Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.
 

Constraints:

2 <= k <= 9
1 <= n <= 60
"""
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        current=[]
        result=[]
        def backtrack(current,k,n,startindex):
            if len(current)==k:
                if sum(current)==n:
                    result.append(current.copy())
                return
            for i in range(startindex,10):
                if i in current:
                    continue
                current.append(i)
                backtrack(current,k,n,i+1)
                current.pop()
            
        backtrack(current,k,n,1)
        return result


"""Approach:
1. Backtracking 
2. Same as all other combination sum problems (39. Combination Sum, 40. Combination Sum II)
3. Except in base condition, put len(current)==k and sum(current)==n
4. In order to  avoid duplicates of lists, pass startindex as an argument in the backtracking function.
5. Start the for loop with the given startindex range.
6. in recursive backtracking call, incrememnt the startindex by 1 on every call (i+1)
 """
