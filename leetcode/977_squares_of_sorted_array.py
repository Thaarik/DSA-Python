# Squares of sorted array - 977
# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

class Solution(object):
    def sortedSquares(self, nums):
        l = 0
        r = len(nums)-1
        res = [0]*len(nums)
        i = len(nums)-1
        while l <= r:
            lv = nums[l]**2
            rv = nums[r]**2
            if rv > lv:
                res[i] = rv
                r -= 1
            else:
                res[i] = lv
                l += 1
            i -= 1
            if i < 0:
                return res
        return nums
    
