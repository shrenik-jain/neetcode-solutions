'''
Question: https://leetcode.com/problems/number-of-islands/
'''

from collections import deque
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        Use BFS Using a Queue

        TC: O(m*n) where m = rows, n = columns
        SC: O(m*n) for the visited set
        '''
        # init the dimensions of the grid
        ROWS, COLS = len(grid), len(grid[0])
        # init a set to keep track of visited cells
        visit = set()
        # count the number of islands
        islands = 0

        def bfs(r, c):
            '''
            BFS to find all the connected islands
            '''
            # directions to move in the grid (up, down, left, right)
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            # init a queue to perform BFS
            q = deque()
            # add the current cell to the queue to start the BFS
            q.append((r, c))
            # mark the cell as visited
            visit.add((r, c))

            # while the queue is not empty i.e there are still connected islands to explore
            while q:
                # pop the most recent cell from the queue
                row, col = q.popleft()

                # for this island, move in all the 4 directions to check for connected 1's
                for dr, dc in directions:
                    r, c = row + dr, col + dc

                    # if the move is within bounds (First 2 conditions) and it is an island (Third condition)
                    # and the cell has not been visited earlier (Fourth condition)
                    if (r in range(ROWS) and 
                        c in range(COLS) and 
                        grid[r][c] == "1" and 
                        (r, c) not in visit ):

                        # add the newly found connected island ("1") to the queue
                        q.append((r, c))
                        # mark the cell as visited
                        visit.add((r, c))

        # iterate over all the cells in the grid
        for r in range(ROWS):
            for c in range(COLS):
                # if the cell is and island i.e "1" and not previous visited, perform BFS
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    # increment the count of islands
                    islands += 1

        # return the final count of islands
        return islands