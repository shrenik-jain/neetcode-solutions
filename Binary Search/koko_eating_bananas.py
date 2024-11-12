'''
Question: https://leetcode.com/problems/koko-eating-bananas/
'''

import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Use Binary Search on k which will range from (1, max(piles)) { since k will range from [1, max(piles)] }

        TC: O( len(piles) * log(max(piles)) )
        SC: O(1)
        """

        # set left = 1 and right = max(piles)
        left, right = 1, max(piles)
        # init res to infinity, to store the min `k`
        res = float('inf')
        
        # while the 2 pointers don't meet
        while left <= right:
            # get the middle value as k
            k = (left + right) // 2
            hours = 0

            # for this k (rate of eating bananas), find num of hours req to eat each pile 
            for p in piles:
                hours += math.ceil(p / k)

            # if required hours <= given hours `h`, we have found a new potential result
            if hours <= h:
                res = min(res, k)
                # since koko can eat bananas at current rate k, find an even smaller rate
                right = k - 1

            # else, req hours > given hours `h`, we have to find a larger rate `k`
            else:
                left = k + 1

        # return the result
        return res
        