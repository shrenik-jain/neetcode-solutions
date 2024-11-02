"""
Question: https://leetcode.com/problems/word-search/
"""

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''
        Use Backtracking DFS

        TC: O( ROWS * COLS * 4^len(words) )
        '''
        # get rows and cols of the board
        ROWS, COLS = len(board), len(board[0])
        # init path (set) to avoid using a cell more than once
        path = set()

        def dfs(r, c, i):
            '''
            Helper DFS function
            '''
            if i == len(word):
                return True

            # if current cell is out of bounds (1st & 2nd conditions) or 
            # current cell not equal to `i`th word (3rd condition) or
            # current cell is previous visited (4th condition)
            if (r not in range(ROWS) or
                c not in range(COLS) or
                board[r][c] != word[i] or
                (r, c) in path):
                
                return False

            # we used the current cell, so add it to the path
            path.add((r, c))

            # check for cells in all 4 directions of current cell
            res = ( dfs(r+1, c, i+1) or 
                    dfs(r-1, c, i+1) or
                    dfs(r, c+1, i+1) or
                    dfs(r, c-1, i+1) )

            # current cell call is complete, remove it from the path
            path.remove((r, c))
            # return `res` (if word is found)
            return res

        # iterate over all cells, and call `dfs()`
        for r in range(ROWS):
            for c in range(COLS):
                # if word found, return True
                if dfs(r, c, 0):
                    return True

        # word not found, return False
        return False
