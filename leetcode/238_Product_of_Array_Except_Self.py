'''
238. Product of Array Except Self
Medium
19.7K
1.1K
Companies
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[]
        zerocount=0
        if(nums[0]!=0):
            prod=nums[0]
        else:
            prod=1
            zerocount=1
        for i in range(1,len(nums)):
            if nums[i]!=0:
                prod=prod*nums[i]
            else:
                zerocount+=1
        if 0 in nums:
            for i in range(len(nums)):
                if nums[i]!=0 or zerocount>1:
                    ans.append(0)
                else:
                    ans.append(int(prod))
        else:
            for i in range(len(nums)):
                    ans.append(int(prod/nums[i]))
        return ans

        '''
        Another Approach

         length = len(nums)
        
        # The answer array to be returned
        answer = [0]*length
        
        # answer[i] contains the product of all the elements to the left
        # Note: for the element at index '0', there are no elements to the left,
        # so the answer[0] would be 1
        answer[0] = 1
        for i in range(1, length):
            
            # answer[i - 1] already contains the product of elements to the left of 'i - 1'
            # Simply multiplying it with nums[i - 1] would give the product of all 
            # elements to the left of index 'i'
            answer[i] = nums[i - 1] * answer[i - 1]
        
        # R contains the product of all the elements to the right
        # Note: for the element at index 'length - 1', there are no elements to the right,
        # so the R would be 1
        R = 1;
        for i in reversed(range(length)):
            
            # For the index 'i', R would contain the 
            # product of all elements to the right. We update R accordingly
            answer[i] = answer[i] * R
            R *= nums[i]
        
        return answer
        '''

            
            
        

