'''
Question: https://leetcode.com/problems/last-stone-weight/
'''

from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        '''
        Use a maxHeap

        Time Complexity: O(n) + O(nlogn)
        Space Complexity: O(n)
        '''
        # create an array of stones (multiplied by -1 since python does not provide a maxHeap)
        maxHeap = [-1 * stone for stone in stones]
        # heapify the array to create a maxHeap
        heapq.heapify(maxHeap)

        # while there are still 2 or more stones in the heap
        while len(maxHeap) > 1:
            # get the 2 heaviest stones
            s1, s2 = -1 * heapq.heappop(maxHeap), -1 * heapq.heappop(maxHeap)

            # if s1 is heavier than s2
            if s1 > s2:
                heapq.heappush(maxHeap, -1 * (s1 - s2))
        
        # if after completing the loop, all stones are destroyed return 0 else return the last remaining stone weight
        return -1 * maxHeap[0] if len(maxHeap) == 1 else 0
                
        