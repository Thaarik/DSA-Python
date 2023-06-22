'''78. Subsets
Medium
14.7K
213
Companies
Given an integer array nums of unique elements, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        current = []
        self.backtrack(nums,current,result,0)
        return result

    def backtrack(self, nums: List[int],current: List[int],result: List[int], startindex: int) -> List[List[int]]:
        result.append(current.copy())
        for i in range(startindex,len(nums)):
            current.append(nums[i])
            self.backtrack(nums, current,result,i+1)
            current.remove(nums[i])

    '''
    Approach: Backtracking 
    1. Same like Permutation
    2. Base case: just add the current list.
    3. in the iteration, start with the given start index and append it inside the current list.
    4. do the recursive backtrack function for the next index.
    5. After the consecutive recursive calls, finish it by removing the inserted value inside the current list
    '''