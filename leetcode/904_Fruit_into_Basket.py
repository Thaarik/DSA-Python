'''
904. Fruit Into Baskets
Medium
3.9K
277
Companies
You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.

 

Example 1:

Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.
Example 2:

Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].
Example 3:

Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].
 

Constraints:

1 <= fruits.length <= 105
0 <= fruits[i] < fruits.length
'''
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        maxFruit, totalFruit = 0,0
        fruitBasket = collections.defaultdict(int)#initilizes the value of the inserted key to zero
        start = 0
        for end in range(len(fruits)):
            fruitBasket[fruits[end]]+=1 #increment the count of the fruit type in the basket
            totalFruit+=1 #total number of current fruit in the basket
            while len(fruitBasket)>2: #if the types of fruit are greater than 2 
                fruitBasket[fruits[start]]-=1 #decrement the start type of the fruit
                totalFruit-=1 #decrement the current fruit count
                if fruitBasket[fruits[start]]==0: #if the start fruit count is below 0, pop it out so that the fruit type number comes below or equal to 2
                    fruitBasket.pop(fruits[start])
                start+=1 # move the start slider to the right 
            maxFruit = max(maxFruit, totalFruit) #get the maximum count in the basket
        return maxFruit


    ''' 
    Approach:
    1. Using sliding window technique.
    2. Create a hashmap (fruit basket) that initializes with 0 value for every key.
    3. Using start and end pointer for the window, first we add the fruit inside the hashmap and increment its count. Increment the total fruit count in the basket
    4. When the hashmap length becomes greater than 2, decrement the fruit count in the start slider until you can move the start slider to the right (increment the start index) and reduce the fruit count inside the basket less than or equal to 2.
    5. Take the max value of total fruits in the basket hashmap.
    '''
        