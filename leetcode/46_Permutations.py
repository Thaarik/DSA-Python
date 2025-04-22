'''
46. Permutations
Medium
16K
262
Companies
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
 

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
'''

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        current = []
        self.backtrack(nums,current,result)
        return result
    
    def backtrack(self,nums: List[int], current: List[int], result: List[int]) -> List[List[int]]:
        if len(current)==len(nums):
            return result.append(current.copy())
        else:
            for i in range(len(nums)):
                if nums[i] in current:
                    continue
                else:
                    current.append(nums[i])
                    self.backtrack(nums,current,result)
                    current.remove(nums[i])

# Approach 1: Backtracking
# Steps:
# 1. Use backtracking to explore all possible permutations
# 2. Maintain two lists: 
#    - Current permutation being built (curr)
#    - Result list to store all valid permutations (res)
# 3. In each recursive call:
#    - If curr is complete (same length as input), add to result
#    - Otherwise, try adding each unused number to curr
#    - Backtrack by removing the last added element before trying next possibility
# 4. Skip elements already in curr to avoid duplicates
# Time: O(n!) - we generate n! permutations
# Space: O(n) - for the recursion stack and current permutation

        # Approach 2
        if len(nums)==0:
            return [[]]
        perm = self.permute(nums[1:])
        res=[]
        for p in perm:
            for i in range(len(p)+1):
                perm_copy = p[:]
                perm_copy.insert(i,nums[0])
                res.append(perm_copy)
        return res
    


# Approach 2: Recursive Insertion
# Steps:
# 1. Base case: empty list returns a list containing empty permutation
# 2. Recursive step:
#    - Extract first element of array (nums[0])
#    - Find all permutations of remaining elements (nums[1:]) recursively
#    - For each permutation found, create new permutations by inserting
#      the first element at every possible position
# 3. Example with [1,2,3]:
#    - Get permutations of [2,3] → [[2,3], [3,2]]
#    - Insert 1 in all positions:
#      * [1,2,3], [2,1,3], [2,3,1]
#      * [1,3,2], [3,1,2], [3,2,1]
# Time: O(n!) - we generate n! permutations
# Space: O(n) - for the recursion stack