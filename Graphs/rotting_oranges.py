'''
Question: https://leetcode.com/problems/rotting-oranges/
'''

from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        Use BFS 

        TC: O(n * m) where n, m are dimensions of the `grid`
        SC: O(n * m) where n, m are dimensions of the `grid`
        '''
        ROWS, COLS = len(grid), len(grid[0])
        # keep track of the time, and number of fresh oranges
        time, fresh = 0, 0
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                # count the number of fresh oranges in the `grid`
                if grid[r][c] == 1:
                    fresh += 1
                # if the orange is rotten, add its coordinates (row, col) to the queue (For BFS)
                if grid[r][c] == 2:
                    q.append([r, c])

        # the directions in which we can move (up, down, right, left)
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        # while there are still rotten oranges in the queue, and fresh oranges in the `grid`
        while q and fresh > 0:
            qLen = len(q)
            for i in range(qLen):
                # pop the most recent rotten orange from the queue
                r, c = q.popleft()
                # for that orange, move in all the directions
                for dr, dc in directions:
                    row, col = r + dr, c + dc

                    # if we moved in directions which are out of bounds, or if the (row, col) is 
                    # not a fresh orange, then move on to the next direction
                    if ((row < 0 or row == ROWS) or 
                        (col < 0 or col == COLS) or 
                        (grid[row][col] != 1)):
                        continue

                    # if above condition is skipped, means we are at a fresh orange, within bounds,
                    # 1. make than orange rotten (replace it with `2`)
                    grid[row][col] = 2
                    # 2. append the newly rotten orange to the q
                    q.append([row, col])
                    # 3. reduce count of fresh oranges by 1
                    fresh -= 1

            # we have completed 1 minute frame, so increase the time by 1
            time += 1

        # if no fresh oranges are left, return the time, else return -1
        return time if fresh == 0 else -1 
