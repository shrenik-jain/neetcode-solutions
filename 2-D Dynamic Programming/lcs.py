'''
Question: https://leetcode.com/problems/longest-common-subsequence/
'''

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ''' Use DP Approach '''

        n1 = len(text1)
        n2 = len(text2)

        # create a dp `lcs` with dimensions equal to (length + 1) of each string
        lcs = [[0] * (n2 + 1) for _ in range(n1 + 1)]

        '''
        Example: text1 = abce  text2: ace
        Initially dp table `lcs` will look like:
        
        r  c-> 0  1  2  3  4
        |      a  b  c  e  _
        0  a               0
        1  c               0
        2  e               0
        3  _   0  0  0  0  0

        We will start at cell (n1-1) and (n2-1) i.e (2nd row, 3rd column) -> (2, 3)
        The last row and column are 0s since these are out of bounds, and serve as a base case
        '''
        # iterate over the length of `text1` in reverse order (bottom-up approach)
        for i in range(n1 - 1, -1, -1):
            # also, iterate over the length of `text2` in reverse order
            for j in range(n2 - 1, -1, -1):

                # if characters in both strings are the same:
                # 1. Add 1 for the current character which is the same
                # 2. now find the longest lcs in the remaining string excluding the same character
                if text1[i] == text2[j]:
                    lcs[i][j] = 1 + lcs[i+1][j+1]

                # if the characters are not the same, find the lcs in 
                # [`text1` (without the ith character) and `text2` (entire string)] and 
                # [`text1` (entire string) and `text2` (without the jth character)] 
                else:
                    lcs[i][j] = max(lcs[i+1][j], lcs[i][j+1])

        # the lcs will be at the first position in the dp table
        return lcs[0][0]
        