'''
Question: https://leetcode.com/problems/longest-palindromic-substring/
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        Check for palindrome by starting in the middle and expanding outwards. 
        We do this by mid = ith index in the string ('i' is each char in the string).
        Remember to check for odd and even both, since the mid will be different in both cases.
        '''
        res = ""

        for i in range(len(s)):
            # Consider `i`th index as the middle element and check if palindrome by moving outwards
            # We consider both cases, i.e. `i` is odd and `i` is even
            
            # For odd length palindromes -> l == r == i, i.e. same middle element
            l, r = i, i
            odd = self.expand(l, r, s)

            # For even length palindromes -> l = i and  r = i+1
            l, r = i, i+1
            even = self.expand(l, r, s)

            # Update the `longest` palindrome string from odd and even checks
            res = max(res, even, odd, key=len)

        # return the longest substring
        return res

    
    def expand(self, l, r, s):
        '''
        Helper method to find expand on both sides of the center and find palindrome between two 
        pointers `l` and `r` in string `s`
        '''

        # Iterate with two pointers outwards, until the characters don't match i.e. end of 
        # palindromic substring. Start in the middle and move pointers in opposite directions
        while(l >= 0 and r < len(s) and s[l] == s[r]):
            l -= 1
            r += 1

        # When the comparison stops, you return the palidrome string
        # i.e. the string in between `l` and `r` pointers (excluding `l` and `r`)
        return s[l+1 : r]
        