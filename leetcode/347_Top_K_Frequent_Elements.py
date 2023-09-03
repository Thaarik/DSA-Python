'''
347. Top K Frequent Elements
Medium
15.8K
555
Companies
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        s = set(nums)
        for i in nums:
            if i in res:
                res[i]+=1
            else:
                res[i]=1
        ans=[]
        res = sorted(res.items(), key=lambda x: x[1])
        for i in res[-k:]:
            ans.append(i[0])
        return ans
    
    '''
    Approach:

    Define the set from the input.
    Create a 'res' hashmap where it stores numbers in input list as keys and its count as value.
    sort the 'res' hashmap
    The last 'k' keys containng the highest count values are the most frequent elements.
    '''
