"""
Question: [Leetcode Premium] -> https://leetcode.com/problems/walls-and-gates
          [Neetcode Free] -> https://neetcode.io/problems/islands-and-treasure
"""

from typing import List
from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        Travel from the chest to the land using BFS, filling
        all the neighbouring cell distances from the chest

        Time Complexity: O(ROWS * COLS)
        Space Complexity: O(ROWS * COLS)
        """
        # get the dimensions of the grid
        ROWS, COLS = len(grid), len(grid[0])
        # init hashset to keep track of already visited cells
        visit = set()
        # maintain a queue for BFS
        q = deque()
        # the current distance from the treasure chest
        distance_from_chest = 0

        def addRoom(r, c):
            """
            BFS helper function which checks all valid 
            neighbouring cells
            """
            # if cell is out of bouds of the matrix or
            # if cell has been already visited or
            # if cell is water (cannot be traversed)
            # is invalid, hence return immediately
            if (r not in range(ROWS) or
                c not in range(COLS) or
                (r, c) in visit or
                grid[r][c] == -1):
                
                return
            
            # if block skipped, means valid cell
            # mark it visited
            visit.add((r, c))
            # append to the queue for next BFS
            q.append([r, c])

        # iterate over all cells, find and add chest cells to 
        # the queue and mark them visited
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))

        # DO BFS
        while q:
            # for current level (num of elements in `q` right now)
            qLen = len(q)
            # iterate over all current cells
            for i in range(qLen):
                r, c = q.popleft()
                # mark the distance of cell from the chest
                grid[r][c] = distance_from_chest

                # do BFS on all the neighbouring cells
                addRoom(r+1, c)
                addRoom(r-1, c)
                addRoom(r, c+1)
                addRoom(r, c-1)

            # one level of queue completed, hence inc the 
            # distance_from_chest
            distance_from_chest += 1
        
