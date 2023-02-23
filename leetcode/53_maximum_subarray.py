'''
53. Maximum Subarray
Medium

Given an integer array nums, find the subarray with the largest sum, and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        # max_ending = 0
        # max_final = -math.inf
        # for i in range(n):
        #     max_ending = max_ending+nums[i]
            
        #     if max_ending>max_final:
        #         max_final = max_ending
        #     if max_ending < 0:
        #         max_ending = 0
        # return max_final
        res = nums[0]
        max_ending = nums[0]
        for i in range(1,n):
            max_ending = max(max_ending+nums[i],nums[i])
            res = max(max_ending,res)
        return res
