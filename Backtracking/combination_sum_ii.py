'''
Question: https://leetcode.com/problems/combination-sum-ii/
'''

from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Backtracking: Take 2 decisions for every element in nums (include or NOT include)
        Also, sort the nums list, so that we can skip duplicate elements

        TC: O(nlogn) + O(n * 2^n) = O(n * 2^n)
        SC: O(1)
        """
        # init the res list
        res = []
        # init a subset list, to store each subset
        subset = []
        # sort the candidates list, so that we can skip duplicate elements
        candidates.sort()

        def dfs(i, total):
            """
            Helper backtracking function
            """
            # edge case, if total = target, append the subset to res and return
            if total == target:
                res.append(subset.copy())
                return

            # edge case, if index `i` is out of bounds or total > target, return
            if i >= len(candidates) or total > target:
                return

            # decision to add ith candidate to subset
            subset.append(candidates[i])
            dfs(i+1, total + candidates[i])

            # while the next index exists, and the candidate @i+1 index == candidate @curr index, skip
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1

            # decision NOT to add ith candidate to subset
            subset.pop()
            dfs(i+1, total)

        # first dfs call with index 0, total 0
        dfs(0, 0)
        return res
        