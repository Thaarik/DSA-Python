'''
169. Majority Element
Easy

Companies
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
 

Follow-up: Could you solve the problem in linear time and in O(1) space?
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # my_dict = {i:0 for i in set(nums)}
        # for i in range(len(nums)):
        #     my_dict[nums[i]]+=1
        #     if my_dict[nums[i]]>=len(nums)/2:
        #         return nums[i]
        ''' Follow up '''
        ''' Boyer-Moore Algo '''
        ''' Set result variable to nums[0]. 
        Incremnet count when the result==nums[i] in every step. 
        If result!=nums[i], decrement the count. 
        When the count goes to zero, set the result == nums[i] and move on. 
        When the foor lop reaches to final nums[i], the resulting result is the answer
        '''
        res = 0
        count = 0
        for i in nums:
            if count==0:
                res = i
            if res == i:
                count+=1
            else:
                count-=1
        return res
