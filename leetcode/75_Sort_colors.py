''' 75. Sort Colors
Medium

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
 

Constraints:

n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.'''

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ''' Bubble sort - compare adjacent element and swap them if thy are in wrong sorted order '''
        # for i in range(len(nums)-1):
        #     for j in range(len(nums)-i-1):
        #         if nums[j]>nums[j+1]:
        #             nums[j],nums[j+1]=nums[j+1],nums[j]
        # print(nums)

        '''Selection sort -continuously check the minimum element and swap them infornt of the array/list'''
        # for outer in range(len(nums)):
        #     min_index = outer
        #     for inner in range(outer+1,len(nums)):
        #         if nums[min_index]>nums[inner]:
        #             min_index = inner
        #     nums[outer],nums[min_index]=nums[min_index],nums[outer]
        #     print(nums)

        ''' Insertion sort - split the app into sorted and unsorted starting with first i element of the array. then check the value of i+1 element in unsored array and sort that element in the sorted array'''
        for i in range(1,len(nums)):
            key = nums[i]
            j=i-1
            while j>=0 and key < nums[j]:
                nums[j+1]=nums[j]
                j-=1
                
            nums[j+1]=key
            print(nums)
            
