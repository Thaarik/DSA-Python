# 704. Binary Search
# Easy

# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums)-1
        while left<=right:
            middle = left+((right-left)//2)
            if nums[middle]>target:
                right = middle-1
            elif nums[middle]<target:
                left = middle+1
            else:
                return middle
        return -1
    

#JavaScript

# var search = function(nums, target) {
#     let low = 0
#     let high = nums.length-1;
#     while(low<=high){
#         let mid = low+Math.floor((high-low)/2);
#         if(nums[mid]===target){
#             return mid;
#         }else if (nums[mid]>target){
#             high=mid-1;
#         }else{
#             low=mid+1;
#         }
#     }
#     return -1;
# };