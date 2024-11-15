'''
Question: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
'''

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Use DFS

        TC: O(n * 4^n) [since at max 4 chars per digit]
        """
        # init res to store the result
        res = []
        # init a hashMap to map digits to their respective characters
        digitToChar = { "2": "abc", 
                        "3": "def",
                        "4": "ghi",
                        "5": "jkl",
                        "6": "mno",
                        "7": "pqrs",
                        "8": "tuv",
                        "9": "wxyz" }

        def dfs(i, currStr):
            """
            helper DFS function
            """
            # if the current string has as many chars as the number of digits, we have found an answer,
            # append it to the result list `res` and return
            if len(currStr) == len(digits):
                res.append(currStr)
                return

            # go over every character corresponding to ith digit in digits
            for c in digitToChar[ digits[i] ]:
                # call dfs() for that char, with the next index, and add curr char to the `currStr`
                dfs(i+1, currStr + c)

        # if the digits string is non-empty, call dfs()
        if digits:
            dfs(0, "")

        # return the final result
        return res
