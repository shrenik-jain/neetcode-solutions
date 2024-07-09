'''
Question: [Leetcode Premium] -> https://leetcode.com/problems/encode-and-decode-strings/
          [Lintcode Free] -> https://www.lintcode.com/problem/659/%20(Free%20by%20Lintcode)
          [Neetcode Free] -> https://neetcode.io/problems/string-encode-and-decode
'''

from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        '''
        Encode the strings to store the length (no of characters) + a delimeter 
        (example #) + the actual string

        Example
        ["neet", "code", "algorithms"]
        res = "4#neet4#code10#algorithms"
        '''
        res = ""
        for s in strs:
            # First store the len of following string (no of characters)
            # Plus a Delimeter (say #)
            # Then the string itself
            res += str(len(s)) + "#" + s
        
        return res

    def decode(self, s: str) -> List[str]:
        '''
        Iterate over the string, as soon as you find a number i.e length of string, store it.
        Then capture the string from after the delimeter (which will be immediately after the number/length)
        uptil the length. 
        '''
        res = []
        i = 0

        # Iterate over the string length
        while i < len(s):
            # set `j` to start from ith character
            j = i
            # continue until you get to the delimeter (#)
            while s[j] != "#":
                j += 1

            # Store the number/length of the upcoming
            # string after the delimeter 
            length = int(s[i:j])

            # add to the list, the string from after the `#` uptil the length
            res.append(s[j+1 : j+1+length])

            # update `i` to point to the next number/length of next string
            i = j + 1 + length

        return res

