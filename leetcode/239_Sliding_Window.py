"""
239. Sliding Window Maximum
Hard
14.5K
469
Companies
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length
"""

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        """ 
        1. Using Deque where the numbers are arranged in monotonically decreasing order.
        2. In the sliding window we are appending each index inside the deque.
        3. When the inserted index's number is greater than previous number, it pops the old number and appends the new number in decreasing order.
        4. when the window is slided, the first element in the window is removed and the incoming element is appended inside the deque and does the above process.
        5. So in the deque collection, it stores only the decreasin order of number for every slided windows and result array is appended with the nums[deque[0]]th element.
        """
        queue = collections.deque()
        start = end = 0
        result = []
        while end < len(nums):
            # pop smaller values from queue's rightmost element
            while queue and nums[queue[-1]]<nums[end]:
                queue.pop()
            queue.append(end)

            # remove left values from window
            if start > queue[0]:
                queue.popleft()

            # append result and slide window
            if (end+1)>=k:
                result.append(nums[queue[0]])
                start+=1
            end+=1
        return result

