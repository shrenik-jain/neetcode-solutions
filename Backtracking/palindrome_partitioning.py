'''
Question: https://leetcode.com/problems/palindrome-partitioning/
'''

from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        Use DFS, and for every partition, check if its palindrome

        TC: O(2^n)
        """
        # init res and parts lists
        res, parts = [], []

        def dfs(i):
            """
            DFS helper function
            """
            # base case: if index i > len(s), we found a valid ans, append it to res and return
            if i >= len(s):
                res.append(parts.copy())
                return

            # iterate from current index to end of the string
            for j in range(i, len(s)):
                # if the partition is a palindrome
                if self.isPalin(s, i, j):
                    # append it to the parts list
                    parts.append( s[i: j+1] )
                    # move to the next dfs
                    dfs(j+1)
                    # current partition dfs complete, so pop it from the parts list
                    parts.pop()

        # start dfs from the first index
        dfs(0)
        return res

    def isPalin(self, s, l, r):
        """
        Check palindrome helper function
        """
        while l < r:
            if s[l] != s[r]:
                return False

            l += 1
            r -= 1

        return True
