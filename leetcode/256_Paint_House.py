"""
There is a row of n houses, where each house can be painted one of three colors: red, blue, or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by an n x 3 cost matrix costs.

For example, costs[0][0] is the cost of painting house 0 with the color red; costs[1][2] is the cost of painting house 1 with color green, and so on...
Return the minimum cost to paint all houses.

 

Example 1:


Input: costs = [[17,2,17],[16,16,5],[14,3,19]]
Output: 10
Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue.Minimum cost: 2 + 5 + 3 = 10.
Example 2:


Input: costs = [[7,6,2]]
Output: 2
 


Constraints:

costs.length == n
costs[i].length == 3
1 <= n <= 100
1 <= costs[i][j] <= 20
"""
def min_cost(self, costs: List[List[int]]) -> int:
        # write your code here
        # costs[house][color]

        dp = [0,0,0]
        for house in range(len(costs)):
            dp1=costs[house][0]+min(dp[1],dp[2])
            dp2=costs[house][1]+min(dp[0],dp[2])
            dp3=costs[house][2]+min(dp[0],dp[1])
            dp=[dp1,dp2,dp3]
        return min(dp)

'''
At every step, we have a CHOICE to choose a color and then see what would be the maximum
at the very end. So we explore all the possible cases, remove the repetitive cases using
memoization, and eventually solve the question by ‘DP’. At every step,
- If you choose red, then choose the min of blue or green from previous row
- If you choose blue, then choose the min of red or green from previous row
- If you choose green, then choose the min of red or blue from previous row
'''