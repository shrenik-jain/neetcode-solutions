'''
Question: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
'''

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Use caching to store the optimal result for each stock price in lsit prices

        # if buy - increment index by 1 (can sell the very next day)
        # if sell - increment index by 2 (sold stock, hence cooldown the next day)

        TC: O(n)
        SC: O(n)
        """
        # cache
        dp = {}

        def transaction(i, buying):
            # edge case -> if index is out of bounds then no profit
            if i >= len(prices):
                return 0

            # use cached memory if available, return the optimal value
            if (i, buying) in dp:
                return dp[(i, buying)]

            # if current state if buying, we have 2 options: buy or cooldown
            if buying:
                # option 1: buy = profit from next transaction - current stock price 
                buy = transaction(i=i+1, buying=not buying) - prices[i]
                # option 2: cooldown -> simply move to the next transaction
                cooldown = transaction(i+1, buying)

                # cache the optimal state of current price
                dp[(i, buying)] = max(buy, cooldown)

            # if current state is selling, we have 2 options: sell or cooldown
            else:
                # option 1: sell = profit from next transaction + current stock price
                sell = transaction(i=i+2, buying=True) + prices[i]
                # option 2: cooldown -> simply move to the next transaction
                cooldown = transaction(i+1, buying)

                # cache the optimal state of current price
                dp[(i, buying)] = max(sell, cooldown)

            # return current profit
            return dp[(i, buying)]

        # start with 0th index and buying state=True
        return transaction(i=0, buying=True)
