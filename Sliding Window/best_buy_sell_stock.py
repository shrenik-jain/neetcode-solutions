'''
Question: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
'''

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        use sliding window to find the best buy and sell prices

        TC: O(n)
        SC: O(1) 
        '''
        # init maxProfit as 0
        maxProfit = 0
        # assume buy and sell as first two prices (indexes)
        buy, sell = 0, 1

        # loop until sell doesn't reach the end of prices list 
        while sell < len(prices):
            
        # if curr_price (or sell) is greater than buy price,
            if prices[buy] < prices[sell]:
                # calculate the profit
                profit = prices[sell] - prices[buy]
                # check if current profit `profit` is greater 
                # than all time profit `maxProfit`
                maxProfit = max(maxProfit, profit)

            # if curr_price (or sell) is less than buy price,
            # assign buy to curr_price
            else:
                buy = sell

            # keep incrementing sell price pointer in hope to 
            # find the best price to sell
            sell += 1

        return maxProfit
        