# 189. Rotate Array
# Medium

# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.


class Solution(object):

    def rotate(self, nums, k):
        n=len(nums)
        k=k%n # sets K to its original state in the array for every roatations
        reverseList(nums,n-k,n-1)
        reverseList(nums,0,n-k-1)
        reverseList(nums,0,n-1)
        return nums
def reverseList(nums,left,right):
        l = left
        r = right
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1
        return nums