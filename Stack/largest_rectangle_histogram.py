'''
Question: https://leetcode.com/problems/largest-rectangle-in-histogram/
'''

from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        Maintain a stack with rules:
        1. If we encounter a histogram with height < one @ top of the stack, start popping until we find a height greater
            than or equal to curr height.
        2. How far left can curr height be extended (stored in the stack), since we need to maximize the area.

        TC: O(n)
        SC: O(n)
        '''
        # a stack to store pairs of [startIndex, height] of each histogram 
        stack = []
        maxArea = 0

        for i, ht in enumerate(heights):
            # start -> index from where we can start extending the current height (how far left can we extend), 
            # since we have to maximize the height
            start = i

            # if we encounter a height < height @ top of the stack, we need to POP
            while stack and stack[-1][1] > ht:
                sIndex, height = stack.pop()
                # height * (i - sIndex) -> area of histogram @ top of the stack
                maxArea = max(maxArea, height * (i - sIndex))
                # since the height @ top of stack > curr height, we can extend curr height to the left
                start = sIndex

            stack.append([start, ht])

        # there might still be histograms in the stack which can be extended to the end of `heights` array
        for i, h in stack:
            # check if any of those histogram area are greater than curr maxArea
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea