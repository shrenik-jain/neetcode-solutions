'''
Question: https://leetcode.com/problems/surrounded-regions/
'''

from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Requirement:
        Do not return anything, modify board in-place instead.

        Description:
        Solve the problem in 3 phases:
        1. Move along the border of the board, and capture all the 'O's and convert them to 'T's (DFS)
        2. Move through the entire board, converting all remaining 'O's to 'X's
        3. Move through the entire board, converting the 'T's back to 'O's

        TC: O(ROWS * COLS)
        SC: O(1)
        """
        # get the dimensions of the board
        ROWS, COLS = len(board), len(board[0])

        def capture(r, c):
            """
            DFS Helper function for Phase 1
            """
            # base case: if out of range of the board or curr cell is not an "O"
            if r not in range(ROWS) or c not in range(COLS) or board[r][c] != "O":
                return

            # convert the "O" -> "T"
            board[r][c] = "T"

            # capture the connected "O"s (in 4 directions) of the current cell "O"
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)


        # PHASE 1: Capture all the "O"s along the border
        for r in range(ROWS):
            for c in range(COLS):
                # if current cell is an "O" and is along the border
                if board[r][c] == "O" and ( r in [0, ROWS - 1] or c in [0, COLS - 1] ):
                    capture(r, c)

        # PHASE 2: Convert remaining "O" -> "X"
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # PHASE 3: Convert remaining "T" -> "O"
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
                    