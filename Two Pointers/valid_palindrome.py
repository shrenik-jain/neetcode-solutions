'''
Question: https://leetcode.com/problems/valid-palindrome/
'''

class Solution:
    def isalphaNum(self, c):
        '''
        will check if the given character is alphaNumeric or not by checking if it is in
        the ascii range of alphabets and numbers
        '''
        return ( 
            ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9') 
        )

    def isPalindrome(self, s: str) -> bool:
        '''
        Keep two pointers left (at beginning) and right (at end) and check if they are 
        1. alphaNumeric
            (i) if not alphaNumeric, increase or decrease that pointer until it is alphaNumeric
        2. equal irresecpective of case

        Time Complexity: O(n)
        Space Complexity: O(1)
        '''
        # init left and right pointers to start and end of string respectively
        l, r = 0, len(s) - 1

        # kepp checking until left and right do not meet or cross each other
        while(l < r):

            # if left is not alphaNum keep incrementing and make sure you do not cross right pointer
            while l < r and not self.isalphaNum(s[l]):
                l += 1

            # if right is not alphaNum keep decrementing and make sure you do not cross left pointer
            while r > l and not self.isalphaNum(s[r]):
                r -= 1

            # check if left and right chars are the same irrespective of the case
            # if not same return false immediately
            if s[l].lower() != s[r].lower():
                return False
            # increase left forward and decrease right backward
            l += 1
            r -= 1
        
        return True
        