'''
40. Combination Sum II
Medium
8.9K
227
Companies
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
 

Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
'''

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        current=[]
        result=[]
        sumCurrent=0
        candidates.sort()
        def backtrack(candidates,target,current,result,index):
            if target == 0:
                result.append(current.copy())
            if target <= 0:
                return
            prev=-1
            for i in range(index,len(candidates)):
                if prev == candidates[i]:
                    continue
                current.append(candidates[i])
                backtrack(candidates,target-candidates[i],current,result,i+1)
                current.pop()
                prev=candidates[i]
        backtrack(candidates,target,current,result,0)
        return result


        # Updated
        def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
            res = []
            current = []
            candidates.sort() # sort the candidates first
            def backtrack(target,i):
                if target==0:
                    res.append(current.copy())
                    return
                if target<0 or len(candidates)==i:
                    return
                    # include candidate
                current.append(candidates[i])
                backtrack(target-candidates[i],i+1)
                # exclude candidate
                current.pop() 
                while i+1 < len(candidates) and candidates[i]==candidates[i+1]: # skip the duplicate candidate in the sorted candidates
                    i+=1
                backtrack(target,i+1)

            backtrack(target,0)
            return res
    # Approach of the updated code::
    # 1. Sort the candidates to make it easier to skip duplicates.
    # 2. Use a backtracking function to explore all possible combinations.
    # 3. If the target becomes zero, add the current combination to the result.
    # 4. If the target becomes negative or we reach the end of the candidates, return.
    # 5. Include the current candidate and call the backtracking function recursively.
    # 6. After returning from the recursive call, exclude the current candidate and skip duplicates.
    # 7. Continue the backtracking process until all candidates are explored.
    # 8. Return the result containing all unique combinations that sum up to the target.
    # Time Complexity: O(n * 2^n)
    # Space Complexity: O(n)
