'''

77. Combinations
Medium
6.2K
189
Companies
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

 

Example 1:

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
Example 2:

Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.
 

Constraints:

1 <= n <= 20
1 <= k <= n
'''

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        current = []
        result = []
        def backtrack(n,k,current,result,index):
            print(f'current: {current} result: {result}')
            if len(current)==k:
                return result.append(current.copy()) 
            for i in range(index,n+1):
                if i in current:
                    continue
                current.append(i)
                backtrack(n,k,current,result,i+1)
                current.remove(i)    
        backtrack(n,k,current,result,1)
        return result

# """
# Approach: Backtracking
# 1. Base case : if current length = k, return the appended result
# 2. For loop range from the given index to the 'n', if i exists, continue. Else Append the i and do backtrack recursive call with the starting index as i+1.
# 3. After successfully returning the appended result and moves back to the previous state, remove the appended i value.
# 4. This is similar to subset problem.
# 5. result for n=4, k=2
# current: [] result: []
# current: [1] result: []
# current: [1, 2] result: []
# current: [1, 3] result: [[1, 2]]
# current: [1, 4] result: [[1, 2], [1, 3]]
# current: [2] result: [[1, 2], [1, 3], [1, 4]]
# current: [2, 3] result: [[1, 2], [1, 3], [1, 4]]
# current: [2, 4] result: [[1, 2], [1, 3], [1, 4], [2, 3]]
# current: [3] result: [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4]]
# current: [3, 4] result: [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4]]
# current: [4] result: [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
# """