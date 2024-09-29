'''
Question: https://leetcode.com/problems/daily-temperatures/
'''

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        Maintain a Monotonic Decreasing Stack. If we ever find a temp greater than the temp at 
        the top of the stack, keep popping from the stack until you find a temp in the stack 
        which is less than or equal to the to the current temp.

        While popping (since we found a temp greater than top of the stack), find the difference 
        b/w the index of the current temp and one on the top of the stack, and add it to the result.

        Note: Monotonic Decreasing means in Decreasing Order, but can have equal values
        Example: [23, 18, 15, 15, 12.....]

        TC: O(n)
        SC: O(n)
        '''
        # init a stack with default 0 values
        res = [0] * len(temperatures)
        # the stack will hold pairs of [temp, index] of current temperature
        stack = []

        for i, temp in enumerate(temperatures):
            # if you encounter a temp > than the one on the top of the stack, you've found a temp that is
            # greater, hence keep popping all the lesser temperatures from the stack
            while stack and temp > stack[-1][0]:
                stackTemp, stackInd = stack.pop()
                # store the difference b/w lesser temp and current temp indices
                res[stackInd] = (i - stackInd)

            # don't forget to store the current [temperature, index] pair in the stack   
            stack.append([temp, i])

        return res