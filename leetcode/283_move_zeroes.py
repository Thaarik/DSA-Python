# 283. Move Zeroes
# Easy

# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array

class Solution(object):
    def moveZeroes(self, nums):
        n=len(nums)
        j=0
        for i in range(n):
            if nums[i]!=0:
                if i!=j:
                    nums[i],nums[j]=nums[j],nums[i]
                j+=1
        return nums