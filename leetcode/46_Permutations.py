'''
46. Permutations
Medium
16K
262
Companies
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
 

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
'''

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        current = []
        self.backtrack(nums,current,result)
        return result
    
    def backtrack(self,nums: List[int], current: List[int], result: List[int]) -> List[List[int]]:
        if len(current)==len(nums):
            return result.append(current.copy())
        else:
            for i in range(len(nums)):
                if nums[i] in current:
                    continue
                else:
                    current.append(nums[i])
                    self.backtrack(nums,current,result)
                    current.remove(nums[i])
''' Approach:
1. Backtracking approach
2. Create current and result list (empty)
3. We  are finding all solutions. So, create a backtrack function. 
4. for every number in the nums list, if the number is already present in the current list, skip, else,append that number into the current,
    and recursively call the backtrack function.
5. When the current list hits the base case, i.e., len of current  == len of nums, then append that current list into the result list. 
6. After the above step, when it comes back to the previous state, the current removes the state's num and moves on the next iteration of   for loop. With this we get all permutation solution.

backtrack level 0:                                      []
backtrack level 1:                [1]                   [2]                    [3]
backtrack level 2:           [1,2]  [1,3]           [2.1]  [2,3]         [3,1]    [3,2]
backtrack level 3:         [1,2,3]  [1,3,2 ]      [2,1,3]  [2,3,1]      [3,1,2]  [3,2,1]
'''