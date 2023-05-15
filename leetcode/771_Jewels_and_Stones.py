'''
771. Jewels and Stones
Easy
4.5K
542
Companies
You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".

 

Example 1:

Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
Example 2:

Input: jewels = "z", stones = "ZZ"
Output: 0
 

Constraints:

1 <= jewels.length, stones.length <= 50
jewels and stones consist of only English letters.
All the characters of jewels are unique
'''

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels=list(jewels)
        stones=list(stones)
        count=0
        for i in range(len(stones)):
            if stones[i] in jewels:
                count+=1
        return count


'''
1. Convert the jewels and stones string into list.
2. Initilize count to 0
3. for each element inside stone array, check whether that element is present in the jewels array and increment the count value.
'''