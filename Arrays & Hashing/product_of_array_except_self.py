'''
Question: https://leetcode.com/problems/product-of-array-except-self/
'''

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        Use prefix and postfix products
        Prefix: product of numbers before the current number
        Postfix: product of numbers after the current number

        Time Complexity: O(n)
        Space Complexity: O(1)
        '''
        n = len(nums)
        # create an array of 1's
        result = [1] * n
        # initialize prefix and postfix values as 1 to calculate product
        prefix = 1
        postfix = 1

        for i in range(n):
            # store the prefix product of ith element in i+1th index
            result[i] = prefix
            # calculate the new prefix by multiplying with current number
            prefix *= nums[i]

        # Example [1, 2, 3, 4]
        # After Prefix product
        # result = [1, 1, 2, 6]
        
        # Iterate in revered order to calculate postfix (like prefix product but in reversed order)
        for i in range(len(nums)-1, -1, -1):
            # store postfix of (i-1)th element in ith index
            result[i] *= postfix
            # calculate new postfix by multiplying with current number
            postfix *= nums[i]

        # result = [1, 1, 2, 6]
        # After postfix product
        # result = [24, 12, 8, 6]
        return result
            
        