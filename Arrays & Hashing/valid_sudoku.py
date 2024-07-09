'''
Question: https://leetcode.com/problems/valid-sudoku/
'''

from collections import defaultdict
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        Maintain a HashSet (hashmap of sets) to check for duplicates in each 
        row, column and sub-square

        Time Complexity: O(n^2) (n = 9)
        Space Complexity: O(3n) 
        '''
        # Create a hashmap to store all nums of a specific row
        # Example {'0': {5, 3, 7}, '1': {6, 1, 9, 5}}
        # where keys `0` is the 0th row, `1` is the first row
        rows = defaultdict(set)

        # Create a hashmap to store all nums of a specific col
        # Example {'0': {5, 6, 8, 4, 7}, '1': {3, 9, 6, 8}}
        # where keys `0` is the 0th column, `1` is the first column
        cols = defaultdict(set)

        # Create a hashmap to store all nums of a specific 3x3 square
        # Example {(0,0): {5, 3, 6, 9, 8}, (0,1): {7, 1, 9, 5}}
        # The key here represents square (0,0), (0,1) etc. We get this by int dividing actual row and 
        # col with 3. Like r=0, c=0, then r//3 and c//3 => (0, 0)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                # Check if element is not "."
                if board[r][c] == ".":
                    continue

                # Check if current element does not occur in row, col or square previsouly
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                
                # Add element in row set, col set and sqaure set
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True