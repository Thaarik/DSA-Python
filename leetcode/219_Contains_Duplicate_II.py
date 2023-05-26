'''
219. Contains Duplicate II
Easy
4.9K
2.6K
Companies
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105
'''

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        table = {} #create hashmap
        for i in range(len(nums)):
            if nums[i] in table and abs(table[nums[i]]-i)<=k: #if the value is present in the hashmap and its previous index and current index satisfies the condition, then return true
                return True
            table[nums[i]]=i #if not then update the table 
        return False