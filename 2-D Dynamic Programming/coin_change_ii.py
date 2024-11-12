'''
Question: https://leetcode.com/problems/coin-change-ii/
'''

from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        Use memoization to lookup values from previous nodes
        """
        # setup a dp for memoization. Will go from indices [0....(amount+1)]
        dp = [0] * (amount+1)
        # ways to get $0 = 1 (edge case)
        dp[0] = 1

        # we iterate over coins list first to make sure current coin won't use previous coins
        # eg. in [1, 2 5], 2 won't be able to use 1 or 5 won't be able to use 1 and 2
        # this way we make sure there are no duplicates like (112), (121), and (211)

        # check for every coin in coins
        for coin in coins:
            # iteration starts from coin-denomination index to end of the dp
            for i in range(coin, len(dp)):
                    # subtract current coin denomination from ith index to get 
                    # preivous combinations (memoization)
                    dp[i] += dp[i-coin]

        # return final amount combinations
        return dp[amount]
