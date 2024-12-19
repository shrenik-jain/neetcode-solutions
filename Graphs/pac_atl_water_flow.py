"""
Question: https://leetcode.com/problems/pacific-atlantic-water-flow/
"""

from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        Traverse from the ocean to the neighbouring values using DFS to find if they can
        flow to the ocean. 
        
        Since we are going in the opp direction (ocean to land), we will check if height 
        of neighbouring cells is greater than current. 

        TC: O(ROWS * COLS) 
        SC: O(ROWS * COLS) 
        """
        # get the dimensions of the matrix
        ROWS, COLS = len(heights), len(heights[0])
        # init 2 hashsets to keep track of visited cells
        pac, atl = set(), set()
        # init res to store cells which can flow to both pacific and atlantic ocean
        res = []

        def dfs(r, c, visit, prevHeight):
            # if current cell is already visited or
            # cell is out of bouds of heights matrix or
            # height of current cell is less than the previous cell (i.e. water can't flow up [opposite direction])
            # then invalid cell, return
            if ((r, c) in visit or
                r not in range(ROWS) or
                c not in range(COLS) or
                heights[r][c] < prevHeight):

                return

            # above if block skipped, means valid cell, hence add to the respective visit set (pac/atl)
            visit.add((r, c))

            # check for cells in all 4 directions of the current cell
            dfs(r+1, c, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])

        
        for c in range(COLS):
            # iterate over the first row, do DFS for each cell for pacific
            dfs(0, c, pac, heights[0][c])
            # iterate over the last row, do DFS for each cell for atlantic
            dfs(ROWS-1, c, atl, heights[ROWS-1][c])
        
        for r in range(ROWS):
            # iterate over the first col, do DFS for each cell for pacific
            dfs(r, 0, pac, heights[r][0])
            # iterate over the last col, do DFS for each cell for atlantic
            dfs(r, COLS-1, atl, heights[r][COLS-1])

        # iterate over all cells in `heights` and check which cells can flow to
        # both the oceans, add those to res
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])

        return res