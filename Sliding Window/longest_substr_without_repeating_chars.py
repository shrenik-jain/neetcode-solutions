'''
Question: https://leetcode.com/problems/longest-substring-without-repeating-characters/
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        Use sliding window which will always have unique (no duplicates) characters
        If you find a duplicate, update the window such that the duplicate is eliminated
        '''
        # init `start` as start of window
        start = 0
        # stores the max length of substring
        maxLength = 0
        # used to make sure window has only unique characters
        charSet = set()

        # the end of the window keeps updating throughout the string `s`
        for end in range(len(s)):
            # if we encounter a duplicate
            while s[end] in charSet:
                # cut down the window from the start unitl the 
                # duplicate is eliminated
                charSet.remove(s[start])
                # keep incrementing till we reach the point where the 
                # duplicate is located, and remove it using above command
                start += 1

            # since the duplicate is eliminated, we can successfully
            # add the new character to the window (and set)
            charSet.add(s[end])
            # check if current window is the longest ever seen
            maxLength = max(maxLength, end - start + 1) 

        return maxLength
    