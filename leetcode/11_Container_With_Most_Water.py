'''
11. Container With Most Water
Medium
24.2K
1.3K
Companies
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        capacity = 0
        while i<=j:
            if height[i]<height[j]:
                capacity = max(capacity,((j-i)*height[i]))
                i+=1
            else:
                capacity = max(capacity,((j-i)*height[j]))
                j-=1            
        return capacity

'''
APPROACH:

1. Two pointer approach
2. Initialize two pointers( beginning and end of the array) and a capacity variable to hold the maximum capacity of water.
3. When height [i] is less than height[j], we get to know that the water is going to hold till height[i] level, 
    so, multiply it with the length of water it can cover (j-i) and hold the maximum value from its current capacity value to its previous capacity value.
3. Do the same vice verse when height [j] <= height[j]. Return the capacity value.
'''