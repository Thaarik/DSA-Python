'''
1482. Minimum Number of Days to Make m Bouquets
Medium
2.7K
72
Companies
You are given an integer array bloomDay, an integer m and an integer k.

You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.

The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.

Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.

 

Example 1:

Input: bloomDay = [1,10,3,10,2], m = 3, k = 1
Output: 3
Explanation: Let us see what happened in the first three days. x means flower bloomed and _ means flower did not bloom in the garden.
We need 3 bouquets each should contain 1 flower.
After day 1: [x, _, _, _, _]   // we can only make one bouquet.
After day 2: [x, _, _, _, x]   // we can only make two bouquets.
After day 3: [x, _, x, _, x]   // we can make 3 bouquets. The answer is 3.
Example 2:

Input: bloomDay = [1,10,3,10,2], m = 3, k = 2
Output: -1
Explanation: We need 3 bouquets each has 2 flowers, that means we need 6 flowers. We only have 5 flowers so it is impossible to get the needed bouquets and we return -1.
Example 3:

Input: bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3
Output: 12
Explanation: We need 2 bouquets each should have 3 flowers.
Here is the garden after the 7 and 12 days:
After day 7: [x, x, x, x, _, x, x]
We can make one bouquet of the first three flowers that bloomed. We cannot make another bouquet from the last three flowers that bloomed because they are not adjacent.
After day 12: [x, x, x, x, x, x, x]
It is obvious that we can make two bouquets in different ways.
 

Constraints:

bloomDay.length == n
1 <= n <= 105
1 <= bloomDay[i] <= 109
1 <= m <= 106
1 <= k <= n
'''

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k > len(bloomDay):
            return -1

        def canMakeBouquets(val,m,flowers,bloomDay): #O(n)
            count=0
            bouquets = 0
            for i in bloomDay:
                if val>=i:
                    count+=1 #for consecutive days
                    if count==flowers: # i.e., count == k, then a bouquet is filled and start the count again from 0
                        bouquets +=1 
                        count=0
                        if bouquets==m: # if the number of filled bouquets has reached the condition, i.e., bouquets == m
                            return True
                else: #if not a consecutive day
                    count=0
            return False
        
        start = min(bloomDay)
        end = max(bloomDay)
        while start<end: #O(log m)
            mid = start+(end-start)//2
            if canMakeBouquets(mid,m,k,bloomDay): #if true, we can assume that the minimum days might be present on the left side of the mid 
                end=mid
            else: #if not then on the right side
                start = mid+1
        return start #total: O(n log m)
    
    """ Approach:
    1. Binary Search Method.
    2. First take the min element as start pointer and max element as end pointer.
    3. First take the mid value which is considered as minimum days to fill the bouquet. 
    4. Check with that mid value with all the days present in the bloomday array. If the consecutive days matches with the m value, the we can say that it can fill a bouquet depending on the k value through 'canMakeBouquets' function.
    5. If 'canMakeBouquets' returns true, then we need to find the further minimum days it can fill the bouquets. so move the end pointer to the mid.
    6. if 'canMakeBouquets' return false, then we can guess that the minimum days must be present after the mid value so move the start pointer to the mid+1 place.
    7. Finally, the start value has the lower bound value, i.e., the minimum days the bouquets can fill. So, return start value.

    """

    