#the min price to buy the stock 
#the max price to sell the stock 
#find the diff btw max and min 
#return profit
#greedy algo

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0

        for i in prices:
            if i < buy:
                buy = i
            else:
                current_profit = i - buy
                profit = max(profit, current_profit)
        return profit
