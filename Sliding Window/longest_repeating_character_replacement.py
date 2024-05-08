'''
Question: https://leetcode.com/problems/longest-repeating-character-replacement/
'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        maintain a window which will always have the max length of same chars
        including k replacements. 
        maintain a hashmap to keep the count of characters in the window
        '''
        # keep the count of each character in the current window
        count = {}
        result = 0
        # start of the window
        start = 0

        # keep moving end of window over the entire string `s`
        for end in range(len(s)):
            # update the count of `end`th character in string
            count[s[end]] = 1 + count.get(s[end], 0)

            # while the number of replacements in current window to get the max
            # length of same chars exceeds the number of allowed replacements `k`
            while end - start + 1 - max(count.values()) > k:
                # update the count of char at `start` since window length reduced
                count[s[start]] -= 1
                # reduce the window from the start
                start += 1

            # check if current window length is the max of all time
            result = max(result, end-start+1)

        return result
        