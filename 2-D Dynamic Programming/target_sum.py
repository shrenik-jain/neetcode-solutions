'''
Question: https://leetcode.com/problems/target-sum/
'''

from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        TC: O(n*t) -> n=len(nums), t=target
        SC: O(n)
        """
        # cache -> maps (index, curr_total): number of ways
        dp = {}


        def backtrack(i, total):
            # edge case -> if index i is out of bounds
            if i >= len(nums):
                return 1 if total == target else 0

            # if cache available, use it
            if (i, total) in dp:
                return dp[(i, total)]

            # 2 decisions -> add current num + subtract current num
            # add the two decision results and cache it for the current index
            dp[(i, total)] =(backtrack(i+1, total+nums[i]) + backtrack(i+1, total-nums[i]))

            return dp[(i, total)]

        return backtrack(0, 0)
