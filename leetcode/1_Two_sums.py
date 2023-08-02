'''
1. Two Sum
Easy
46.2K
1.5K
Companies
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            c = target - nums[i]
            if c in hashmap:
                return [i,hashmap[c]]
            hashmap[nums[i]]=i

'''
APPROACH:

1. Create a Hashmap
2. For every element inside the array, subtract that element from the target value. 
3. The value we get from that subtraction is checked with the hashmap.
4. If that subtracted element is present in the hashmap, then return the value(index). Else, add that array element as key and its index as value in the hasmap.

'''

'''
Javascript

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let hashmap = new Map();
    for (let i=nums.length-1;i>=0;i--){
        let diff = target-nums[i];
        if(hashmap.has(nums[i])){
            return [hashmap.get(nums[i]),i]
        }
        hashmap.set(diff,i)
    }
};
// we are going to store the difference between target and current nums[i] value as key and the index i as value.we are returning the answer when nums[i] is present in the keys of the hashmap.
'''