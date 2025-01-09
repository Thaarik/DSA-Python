'''
739. Daily Temperatures
Solved
Medium
Topics
Companies
Hint
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
 

Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100

'''

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # append temperature and index pair (t,i)
        ans = [0]*len(temperatures)
        for index,temp in enumerate(temperatures):
            while stack and temp>stack[-1][0]: # stack[-1][0] is the top element element and we are retreiving the t from (t,i) pair       
                sTemp, sIndex = stack.pop()
                ans[sIndex]=index-sIndex
            stack.append((temp,index))
        return ans

'''Approach:
1. Use Monotonically decreasing stack. Create a result list conatining zeroes of length equal to the input temperatures list.
2. append the stack with the temperature and its index from the input temperatures list.
3. While traversing, append the stack with the decreasing temperature.
3. When it faces the higher value temperature, pop the top element of the stack, and update the result (ans) list by updating the required index's value (0) with the value of difference of current traversed index by the popped out stack's index.
4. Return the ans
'''

'''
Example with print:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Print: print(stack, ans)

[(73, 0)] [0, 0, 0, 0, 0, 0, 0, 0]
[(74, 1)] [1, 0, 0, 0, 0, 0, 0, 0]
[(75, 2)] [1, 1, 0, 0, 0, 0, 0, 0]
[(75, 2), (71, 3)] [1, 1, 0, 0, 0, 0, 0, 0]
[(75, 2), (71, 3), (69, 4)] [1, 1, 0, 0, 0, 0, 0, 0]
[(75, 2), (72, 5)] [1, 1, 0, 2, 1, 0, 0, 0]
[(76, 6)] [1, 1, 4, 2, 1, 1, 0, 0]
[(76, 6), (73, 7)] [1, 1, 4, 2, 1, 1, 0, 0]
'''

        
