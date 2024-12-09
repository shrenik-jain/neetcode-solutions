'''
Question: https://leetcode.com/problems/coin-change/ 
'''

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        ''' Use a bottom up approach i.e. DP approach -> Time Complexity = O (amount * num of coins)'''
        
        # Init `dp` of size `amount` with each initial set at max (can use either infinity or amount + 1 for this)
        dp = [float('inf')] * (amount + 1)
        # Base case - amount 0 will require zero coins
        dp[0] = 0

        # Iterate over the amount, starting at 1 (bottom-up)
        for a in range(1, len(dp)):
            # Also iterate over the coins available
            for c in coins:
                # check if current amount `a` is greater or equal to the coin value `c` present
                if a >= c:
                    # Update the value in 'dp[a]'
                    # `1` is added since we use the current coin `c` for getting the current result.
                    # So dp[a] will store the value of the min of itself and the new value 
                    # i.e. 1+dp[a-c] (using the previous value from the DP)
                    dp[a] = min(dp[a], dp[a-c] + 1)

        # Return the solution stored in dp[-1] only if it is not the default value we had saved,
        # cause if default value in dp[-1], then we could not find a solution so we return -1
        return dp[-1] if dp[-1] != float('inf') else -1