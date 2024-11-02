"""
Question: https://leetcode.com/problems/rotate-image/
"""

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        Step 1: Transpose the Matrix
        Step 2: Reverse each row in Matrix
        """
        n = len(matrix)

        # transpose the matrix (row becomes column, and vice versa)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # reverse each row in the matrix
        for i in range(n):
            matrix[i] = matrix[i][::-1]
 