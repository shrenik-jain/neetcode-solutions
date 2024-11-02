"""
Question: https://leetcode.com/problems/spiral-matrix/description/
"""

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        '''
        Keep 4 pointers left, right, top, bottom to maintain the bounds

        TC: O(ROWS * COLS)
        SC: O(1)
        '''
        res = []
        # left -> 0, right -> 1 col ahead of the matrix
        left, right = 0, len(matrix[0])
        # top -> 0, bottom -> 1 row below of the matrix
        top, bottom = 0, len(matrix)

        # Until No Pointers Meet
        while left < right and top < bottom:

            # get every `i` in the top row (from left to right)
            for i in range(left, right):
                res.append(matrix[top][i])
            
            # got top elements, decrease the top bound by 1
            top += 1

            # get every `i` in the right column (from top to bottom)
            for i in range(top, bottom):
                res.append(matrix[i][right-1])

            # got right elements, decrease the right bound by 1
            right -= 1

            # check condition for single column or single row
            if not (left < right and top < bottom):
                break

            # get every `i` in the bottom row (from right to left)
            for i in range(right-1, left-1, -1):
                res.append(matrix[bottom-1][i])

            # got bottom elements, decrease bottom bound by 1 
            bottom -= 1

            # get every `i` in the left column (from bottom to top)
            for i in range(bottom-1, top-1, -1):
                res.append(matrix[i][left])

            # got left elements, decrease left bound by 1
            left += 1

        return res
            