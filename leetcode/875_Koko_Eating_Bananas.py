"""
875. Koko Eating Bananas
Medium
7.8K
370
Companies
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

 

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23
 

Constraints:

1 <= piles.length <= 104
piles.length <= h <= 109
1 <= piles[i] <= 109
"""

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles)>h:
            return -1
        left = 1
        right = max(piles)
        res =right
        while left<=right:
            k = left+(right-left)//2
            hoursToComplete = 0
            for p in piles:
                hoursToComplete += math.ceil(p/k)
            if hoursToComplete <= h:
                res = min(res,k)
                right=k-1
            else:
                left=k+1
        return res

    
""" Approach:
    1. Binary Search Approach
    2. In order to find the minimum number of Hours we are doing binary search from 1 to max of piles array, i.e., the maximum number of bananas k Koko can eat per hour. Our Objctive is to find the minimum number of hours to eat as much banana as she can in all piles.
    3. So, in that binary search, for every mid value, we assume that as k value (number of bananas koko eats per hour), and using that k value, we are calculating the total number of hours koko takes to complete the whole pile. If k = 6, then in the pile of [3,6,7,11], the total number of hours = (3/6) + (6/6) + (7/6) + (11/6) = 4 < 8 (given h). So form the result we can currently say that K=6 is the minimum number of hours required for koko to eat all the piles. Don't forget to round up the division of each piles with k.
    4. We can assume that there might be even lower k that satisfies the above condition, so we move the right pointer = mid-1.
    5. If the above condition does not satisfies, i.e., k>h, then koko cannot finish all the piles with the given k, so we must find the k(mid) to the right side. So, move the left pointer to the mid+1
    6. return the minimum k value.
"""

            