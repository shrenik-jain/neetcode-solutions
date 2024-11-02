'''
Question: https://leetcode.com/problems/climbing-stairs/
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        Use DP Memoization to cache/store the previously computed subproblems

        TC: O(n)
        SC: O(1)
        '''

        # two variables to store the previous two values
        # We do not use an array, since we only require the previous two values to calculate the new value
        one_step = 1    # os
        two_step = 1    # ts

        # iterate till 0th step
        for i in range(n-1):
            # add previous two steps to find the new step val
            temp = one_step + two_step
            two_step = one_step
            one_step = temp

        return one_step
        

    # Dry Run
    """
    # n = 4
    # res = [0,  0,  0,  1,  1]
    # iter1              os  ts

    # res = [0,  0,  2,  1,  1]
    # iter2          os  ts

    # res = [0,  4,  2,  1,  1]
    # iter3      os  ts

    # res = [6,  4,  2,  1,  1]
    # iter3  os  ts
    """