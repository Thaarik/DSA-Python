'''
287. Find the Duplicate Number
Solved
Medium
Topics
Companies
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

 

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
 

Constraints:

1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.
 

Follow up:

How can we prove that at least one duplicate number must exist in nums?
Can you solve the problem in linear runtime complexity?
'''

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow1 = 0
        fast = 0
        while True:
            slow1 = nums[slow1]
            fast = nums[nums[fast]]
            if slow1 == fast:
                break
        slow2=0
        while True:
            slow1=nums[slow1]
            slow2=nums[slow2]
            if slow1==slow2:
                return slow1

'''
Approach:

1. This problem can also modified like thsi -> Find the intersecting node in the cyclic LinkedList
2. This is based on Floyd's cycle detection/ Hare and the Tortoise.
3. Consider the given array as arrays where each element denotes the indx of next array, i.e., for [1,3,4,2,2] , it denotes 1(0) -> 3(1) ->2(3) -> 4(2) -> 2(4) ->4(2)->2(4)->...... This forms a cycic LinkedList
3. Always keep in mind that the distance between the first node to the intersecting node(Node where the cycle starts) and the distance between the intersecting node and the node where the slow and the fast pointer first meet is always same.
4. By this logic, we can easily find the intersecting node(i.e., the duplicate value). return that intersecting node.

'''

        
        