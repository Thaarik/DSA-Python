'''
922. Sort Array By Parity II
Easy
2.3K
84
Companies
Given an array of integers nums, half of the integers in nums are odd, and the other half are even.

Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.

Return any answer array that satisfies this condition.

 

Example 1:

Input: nums = [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
Example 2:

Input: nums = [2,3]
Output: [2,3]
 

Constraints:

2 <= nums.length <= 2 * 104
nums.length is even.
Half of the integers in nums are even.
0 <= nums[i] <= 1000
 

Follow Up: Could you solve it in-place?
'''
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        if len(nums)==1:
            return nums
        i,j=0,0
        while i<=j and j<len(nums):
            j+=1
            if nums[i]%2==i%2:
                i=j
            else:
                if nums[j]%2==i%2:
                    nums[i],nums[j]=nums[j],nums[i]
                    i+=1
                    j=i
        return nums
'''
Approach:

1. Two pointer approach i, j where initially i=j=0
2. While traversing, first increment j.
3. If number in index i are in place even or odd index, just i = j and move on.
4. If not, check if number in j index satisfies the odd or even index of i. 
    If it satisfies, swap that number in place of j index to i index. 
    Then incremenent ith index and equalize jth index to ith index to check remaining numbers.
5. Return the nums array.
'''