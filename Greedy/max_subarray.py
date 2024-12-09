'''
Question: https://leetcode.com/problems/maximum-subarray/
'''

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        Use Kadane's Algorithm 

        TC: O(n)
        SC: O(1)
        '''
        # init `curSum` and `maxSum` to first element in `nums`
        curSum = maxSum = nums[0]

        # iterate through all elements in nums starting from 2nd postion
        for n in nums[1:]:
            # if the ongoing sum is negative, it will not serve any purpose, so we drop the sum, and make it 0
            if curSum < 0:
                curSum = 0
            # add the current number to ongoing sum `curSum`
            # Note: if the above if condition is satisfied (if `curSum` is negative), the curSum will start from 
            # current number `n`
            curSum += n

            # we have to update the overall maxSum 
            maxSum = max(maxSum, curSum)

        return maxSum
        