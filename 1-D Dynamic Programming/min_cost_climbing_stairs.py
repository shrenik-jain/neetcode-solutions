'''
Question: https://leetcode.com/problems/min-cost-climbing-stairs/
'''

from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
        Use DP

        TC: O(n)
        SC: O(1)
        '''
        # append 0 as the topmost stair [10, 15, 20] -> [10, 15, 20, 0]
        cost.append(0)

        # start iteration from the 2rd last stair (excluding top floor), since we can take 1 or 2 jumps
        for i in range(len(cost)-3, -1, -1):
            # which is better? Taking 1 jump or 2 jumps
            cost[i] += min(cost[i+1], cost[i+2])

        # which is better? starting at step 0 or step 1
        return min(cost[0], cost[1])
        