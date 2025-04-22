'''
90. Subsets II
Solved
Medium
Topics
Companies
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
'''
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        nums.sort()
        def backtrack(index):
            if index==len(nums):
                res.append(subset[:])
                return
            # All subsets that includes nums[i]
            subset.append(nums[index])
            backtrack(index+1)
            subset.pop()
             # All subsets that does not include nums[i]
            while index+1 < len(nums) and nums[index]==nums[index+1]: # skip duplicates in nums
                index+=1
            backtrack(index+1)
        backtrack(0)
        return res
    # Approach:
    # 1. Sort the input array to handle duplicates
    # 2. Use backtracking to generate all subsets
    # 3. Maintain a current subset and a result list
    # 4. In each recursive call:
    #    - If the index is equal to the length of nums, add the current subset to the result
    #    - Include the current number in the subset and call backtrack with the next index
    #    - After backtracking, remove the last number from the subset
    #    - Skip duplicates by incrementing the index until the next unique number
    # 5. Call backtrack with the next index without including the current number
    # 6. Return the result list containing all unique subsets
# Time Complexity: O(2^n) - all possible subsets
# Space Complexity: O(n) - for the subset list

