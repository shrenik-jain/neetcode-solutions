"""
Question: https://leetcode.com/problems/happy-number
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        '''
        Maintain a HashSet to keep track of already calculated sumOfSquares of digits.
        If we ever encounter a 1, return True
        If we ever encounter a number already present in the HashSet, return False
        '''
        # maintain a hastset to keep track of already computed values
        seen = set()

        # continue until you encounter an already computed value present in `seen`
        while n not in seen:
            # add the number to `seen` set
            seen.add(n)
            # find the sum of squares of the digits of the number
            n = self.sumOfSquares(n)
            # if the number is 1, we found a happy number, return True
            if n == 1:
                return True

        # if the above loop terminated, we encountered a value already present in `seen`, hence return False 
        return False
    

    def sumOfSquares(self, n):
        '''
        Helper function to find sum of squares of the digits of `n`
        '''
        output = 0
        # continue until n > 0
        while n:
            # extract the unit's place digit, sqaure it, and add it to output
            output += (n % 10) ** 2
            # remove the unit's place digit, and repeat
            n //= 10

        return output 