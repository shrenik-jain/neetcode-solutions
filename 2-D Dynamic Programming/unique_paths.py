'''
Question: https://leetcode.com/problems/unique-paths/
'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ''' Use DP Approach '''

        # create a dp array with `n` columns and `m` rows
        paths = [[0] * n for _ in range(m)]

        # iterate through each row
        for i in range(m):
            # for every row, iterate through each column
            for j in range(n):
                # if first row or first column, only 1 possible way to reach the goal (bounds of `paths` defined) 
                if i == 0 or j == 0:
                    paths[i][j] = 1

                # if not, add the upper row ([i-1][j]) and left column ([i][j-1]), since the robot can move either down or right
                else:
                    paths[i][j] = paths[i-1][j] + paths[i][j-1]

        # the final solution will be stored in the bottom-right corner
        return paths[m-1][n-1]