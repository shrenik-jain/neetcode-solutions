'''
Question: https://leetcode.com/problems/max-area-of-island/
'''

from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
        Use DFS

        TC: O(m*n) where m = rows, n = columns
        '''
        ROWS, COLS = len(grid), len(grid[0])
        maxArea = 0
        # to keep track of the visited cells
        visit = set()

        def dfs(r, c):
            '''
            Helper function that performs actual DFS
            '''
            # Base Case: If current row or column is out of bounds, or cell is water or cell is already visited
            if (r < 0 or r == ROWS) or (c < 0 or c == COLS) or grid[r][c] == 0 or (r, c) in visit:
                return 0
            
            # mark the current cell as visited
            visit.add((r, c))

            # add 1 for the current island cell + recursively call `dfs()` in all 4 directions for the current cell
            return (1 + dfs(r + 1, c) + 
                        dfs(r - 1, c) +
                        dfs(r, c + 1) +
                        dfs(r, c - 1))

        # iterate over all cells
        for r in range(ROWS):
            for c in range(COLS):
                # find area of current island `dfs()` and check if it is greater than maxArea
                maxArea = max(maxArea, dfs(r, c))

        return maxArea