'''
Question: https://leetcode.com/problems/search-a-2d-matrix/
'''

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Run Binary Search twice:
        1. For Rows, finding in which row does the target value fall
        2. In that row, find the target value

        TC: O(log(COLS)) + O(log(ROWS))
        SC: O(1)
        """
        ROWS, COLS = len(matrix), len(matrix[0])

        # 1st Binary Search to find the ROW where the target value falls

        # get the top and bottom row indices
        top, bottom = 0, ROWS - 1

        while top <= bottom:
            # calculate the middle row
            mid_row = (top + bottom) // 2
            
            # if the target > last element of mid row, check in the lower half 
            if target > matrix[mid_row][-1]:
                top += 1

            # if the target < first element o the mid row, check in the upper half
            elif target < matrix[mid_row][0]:
                bottom -= 1

            # we found the target row
            else:
                break


        # the loop must've exited, without finding the target row, so a check!
        if not (top <= bottom):
            return False


        # 2nd Binary Search to find the target value in the mid_row

        # get the target_row (aka mid_row)
        target_row = (top + bottom) // 2

        # set the left and right pointers
        left, right = 0, COLS - 1

        while left <= right:
            mid = (left + right) // 2

            if target > matrix[target_row][mid]:
                left += 1
            
            elif target < matrix[target_row][mid]:
                right -= 1

            else:
                return True

        return False
