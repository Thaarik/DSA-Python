"""
33. Search in Rotated Sorted Array
Medium
21.4K
1.3K
Companies
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
 

Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        while start<=end:
            mid = start+(end-start)//2
            if nums[mid]==target:
                return mid
            elif nums[start]<=nums[mid]:
                if target<=nums[mid] and target>=nums[start]:
                    end=mid-1
                else:
                    start=mid+1
            else:
                if target>=nums[mid] and target<=nums[end]:
                    start=mid+1
                else:
                    end=mid-1
        return -1

"""
Approach:
1. Binary Search Approach
2. By taking mid element, Check if the starting element <= mid element (that is the elements are sorted are not due to rotation), then if target element is in between the start and mid element, then shift end pointer to mid -1. Else, shift start pointer to mid +1
3. Vice versa.

"""