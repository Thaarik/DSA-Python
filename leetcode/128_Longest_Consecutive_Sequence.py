'''
128. Longest Consecutive Sequence
Medium
18K
800
Companies
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longcount = 0
        sortednums = set(nums)
        for num in nums:
            # check if the num is the starting sequence by checking if there is no predecessor for the given number.
            if num-1 not in sortednums:
                length=1
                while num+length in sortednums:
                    length+=1
                longcount=max(longcount,length)
        return longcount


'''
Approach:

sort the array by uusing set() having O(1) in average case and O(n) in worst case.
for each number in the set, find the starting num that does not has any predecessor to start the consecutive sequence.
do the same for every starting number in the set and find the highest count.

'''