"""
47. Permutations II
Medium
7.7K
131
Companies
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10
"""

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        current = []
        result = []
        count = Counter(nums)
        nums.sort()
        # def backtrack(nums,current,result):
        #     print(nums, current, result)
        #     if not nums:
        #         return result.append(current.copy())
        #     prev=-1
        #     for i in range(len(nums)):
        #         if i>0 and prev==nums[i]:
        #             continue
        #         current.append(nums[i])
        #         backtrack(nums[:i]+nums[i+1:],current,result) # slice the nums array where it removes the element used in prevous recursive call
        #         current.pop()
        #         prev=nums[i]

        # Another approach
        def backtrack(nums, current,result):
            if len(nums)==len(current):
                return result.append(current.copy())
            for c in count:
                if count[c]>0:
                    count[c]-=1
                    current.append(c)
                    backtrack(nums,current,result)
                    count[c]+=1
                    current.pop()
        
        backtrack(nums,current,result)
        return result
    
    TC:O(n * 2^n)