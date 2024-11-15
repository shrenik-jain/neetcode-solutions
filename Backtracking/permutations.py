'''
Question: https://leetcode.com/problems/permutations/
'''

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Use DFS

        TC: O(n!)
        SC: O(n)
        """
        # init res, perms lists
        res, perms = [], []

        def dfs():
            """
            DFS Helper function
            """
            # base case: if perms has all the numbers from nums, we have 1 permutation. Append it to `res`
            if len(perms) == len(nums):
                res.append(perms.copy())
                return

            # iterate over all numbers in nums, and do dfs for all numbers which are not already in `perms`
            for n in nums:
                if n not in perms:
                    # add the current n, and do dfs
                    perms.append(n)
                    dfs()
                    # dfs for current n complete, so pop it from the perms list
                    perms.pop()

        dfs()
        return res
    