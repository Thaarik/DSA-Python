'''121. Best Time to Buy and Sell Stock
Easy

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        res = 0
        for i in range(len(prices)):
            minimum = min(prices[i],minimum) #picks minimum valued stock
            res = max(res,prices[i]-minimum) #max value by selling the highest value stock with picked minimum valued stock
        return res
            

#JavaScript
# var maxProfit = function(prices) {
#     let buy = prices[0]
#     let profit = 0
#     for(let i=0;i<prices.length;i++){
#         buy = Math.min(buy,prices[i]);
#         profit=Math.max(profit,prices[i]-buy);
#     }
#     return profit;
# };