'''
15. 3Sum
Medium
28.2K
2.5K
Companies
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i,a in enumerate(nums):
            if i>0 and a==nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1
            while l<r:
                threesum = a + nums[l]+nums[r]
                if threesum > 0:
                    r-=1
                elif threesum < 0:
                    l+=1
                else:
                    res.append([a,nums[l],nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
        return res

'''

Approach:

Similar to two sums and two sums II.
Sort the input list.
First start with the first element in the list. If the successor is same, shift till its successor is not same.
After shifting, the element is named as 'a'. Now do the Two sum II method for the remaining elements by doing two pointers. The goal is to set a + nums[l] + nums[r] =0 and append those three elements in the res list. 
If the threesum =0 , we need to shift the left 'l' pointer to it's successor but if they are equal, then we need to shift till the successor is not equal to current element so that it does not create any duplicates. No problem with 'r' pointer for finding duplicates.

'''