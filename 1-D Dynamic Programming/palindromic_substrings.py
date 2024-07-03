'''
Question: https://leetcode.com/problems/palindromic-substrings/
'''

class Solution:
    def countSubstrings(self, s: str) -> int:
        '''
        Approach 1: Count even and odd in different loops and combine the results from both
        Time Complexity: Linear O(n) (recheck but pretty sure it's correct!)
        '''
        res = 0
        
        # Count odd length palidromes
        for i in range(len(s)):
            # For odd length palindromes -> l == r == i
            res += self.expand(i, i, s)
            # For even length palindromes -> l = i and  r = i+1
            res += self.expand(i, i+1, s)
            
        return res
    
    # Helper function to find palindromes between two pointers `l` and `r`, given a string `s`
    def expand(self, l, r, s):
        count = 0
        # Start at the same midpoint and expand outwards (in opposite directions)
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
        
        return count