'''
Question: https://leetcode.com/problems/subsets-ii/
'''

from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
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
        # sort the nums list, so that we can skip duplicate elements
        nums.sort()

        def dfs(i):
            """
            Helper backtracking function
            """
            # edge case, if index `i` is out of bounds, store the subset in the res, and return
            if i >= len(nums):
                res.append(subset.copy())
                return

            # decision to include nums[i]
            subset.append(nums[i])
            # dfs call to the next index
            dfs(i+1)

            # while the next index exists, and the element @i+1 index == element @curr index, skip
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1

            # decision NOT to include nums[i]
            subset.pop()
            # dfs call to the next index
            dfs(i+1)

        # first dfs call with index 0
        dfs(0)
        return res
    