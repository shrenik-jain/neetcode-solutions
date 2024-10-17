"""
Question: https://leetcode.com/problems/permutation-in-string

Ref Video: https://www.youtube.com/watch?v=quSfR-uwkZU
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        TC: O(n)
        SC: O(1)
        '''
        # init two array to store the count of chars in s1 and s2 (an array of 26 alphabets)
        countS1, countS2 = [0] * 26, [0] * 26
        n1, n2 = len(s1), len(s2)

        # Edge Case
        if n1 > n2: 
            return False

        # iterate over len(s1) and init countS1 and countS2
        for i in range(n1):
            countS1[ord(s1[i]) - ord('a')] += 1
            countS2[ord(s2[i]) - ord('a')] += 1

        # if all chars match in s1 and s2, return True
        if countS1 == countS2:
            return True

        # since we previously iterated till n1 (line 17), we start from where we left off i.e. `n1`
        for i in range(n1, n2):
            # add the new character count to countS2 (from the right of the window)
            countS2[ord(s2[i]) - ord('a')] += 1
            # remove the old character count to countS2 (from the left of the window)
            countS2[ord(s2[i-n1]) - ord('a')] -= 1

            # if all chars match in s1 and s2, return True
            if countS1 == countS2:
                return True

        # counts don't match until the entire loop, hence return False
        return False