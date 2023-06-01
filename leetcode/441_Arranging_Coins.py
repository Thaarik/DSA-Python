'''
441. Arranging Coins
Easy
3.3K
1.2K
Companies
You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.

 

Example 1:


Input: n = 5
Output: 2
Explanation: Because the 3rd row is incomplete, we return 2.
Example 2:


Input: n = 8
Output: 3
Explanation: Because the 4th row is incomplete, we return 3.
 

Constraints:

1 <= n <= 231 - 1
'''

class Solution:
    def arrangeCoins(self, n: int) -> int:
        left = 1
        right = n
        res = 0
        while left<=right:
            mid = (left+right)//2
            coins = (mid*(mid+1)//2)
            if coins>n:
                right=mid-1
            else:
                left=mid+1
                res = max(res,mid)
        return res


        """
        Approach:

        1. Binary Search.
        2. take left pointer from the start and right pointer at n.
        3. No take the mid pointer and apply Gauss formula (n*(n+1)/2)
        4. When th value of the formula is larger than the n value, it means that the number of coins are larger than the number of rows it can accomodate. SO shift right pointer to the mid-1
        5. If the value of the forula is lesser than then n value, the number of coins are lesser than the number it can accomodate in the rows. SO take the max value from it and move on. The max resut is the result denoting the maximum number of the rows the coin can cover entirely.
        """