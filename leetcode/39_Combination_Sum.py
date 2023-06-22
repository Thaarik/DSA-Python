'''
39. Combination Sum
Medium
16.3K
328
Companies
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
frequency
 of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []
 

Constraints:

1 <= candidates.length <= 30
2 <= candidates[i] <= 40
All elements of candidates are distinct.
1 <= target <= 40
'''

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        current = []
        currentSum = 0
        self.backtrack(candidates,target,result, current,currentSum,0)
        return result

    def backtrack(self, candidates: List[int], target: int, result: List[int], current: List[int] ,currentSum: int, startindex: int) -> List[List[int]]:
        curr = current.copy()
        if currentSum==target:
            return result.append(curr)
        elif currentSum>target:
            return
        else:
            for i in range(startindex, len(candidates)):
                current.append(candidates[i])
                self.backtrack(candidates,target,result,current,currentSum+candidates[i],i) # not i+1 because we are reusing the candidates[i]
                current.remove(candidates[i])

'''Approach: Backtracing

1. Same like subset (78. Subsets) except we are reusing the candidates value and finding all solutions.'''