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
        # Correct approach
        # initial
        ans = [1]*len(nums)
        # initial prefix value
        prefix = 1
        for i in range(len(nums)):
            ans[i]=prefix
            prefix*=nums[i]

        # initial postfix value
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            ans[i]*=postfix
            postfix*=nums[i]
        return ans  

''' Approach:

Start by initializing a prefix variable to 1 and iterate through the input array. 
For each position in the output array, they store the prefix value and then multiply it by the corresponding input array value. 
Then repeat the process in reverse order with a postfix variable, but instead of storing the postfix value directly, they multiply it with the existing value in the output array. 
Finally, they return the output array as the result.

'''

        # ans=[]
        # zerocount=0
        # if(nums[0]!=0):
        #     prod=nums[0]
        # else:
        #     prod=1
        #     zerocount=1
        # for i in range(1,len(nums)):
        #     if nums[i]!=0:
        #         prod=prod*nums[i]
        #     else:
        #         zerocount+=1
        # if 0 in nums:
        #     for i in range(len(nums)):
        #         if nums[i]!=0 or zerocount>1:
        #             ans.append(0)
        #         else:
        #             ans.append(int(prod))
        # else:
        #     for i in range(len(nums)):
        #             ans.append(int(prod/nums[i]))
        # return ans


        
            
            
        