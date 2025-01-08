"""sumary_line
42. Trapping Rain Water
Solved
Hard
Topics
Companies
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l, r = 0, len(height) - 1
        l_max, r_max = height[l], height[r]
        res = 0
        while l < r:
            if l_max < r_max:
                l += 1
                l_max = max(l_max, height[l])
                res += l_max - height[l]
            else:
                r -= 1
                r_max = max(r_max, height[r])
                res += r_max - height[r]
        return res

'''
Explaination: Two pointers
1. Initialize two pointers l and r to point to the first and last element of the input array height.
2. Initialize two variables l_max and r_max to store the maximum height of the left and right subarray.
3. Iterate the input array height until l < r.
4. If l_max < r_max, move the pointer l to the right and update l_max to the maximum height between l_max and height[l].
5. Otherwise, move the pointer r to the left and update r_max to the maximum height between r_max and height[r].
6. Add the difference between the current maximum height and the current height to the result.
7. Return the result.
Time complexity: O(n)
Space complexity: O(1)
'''