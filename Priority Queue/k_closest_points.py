'''
Question: https://leetcode.com/problems/k-closest-points-to-origin/
'''

import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Calculate distance of each point from the origin and append to a minHeap -> [dist, x, y]
        Get the k points with least distance from the minHeap, and append to the `res` list

        Time Complexity: O(n) + O(nlogn)
        Space Complexity: O(n)
        """
        # init minHeap and res list
        minHeap, res = [], []

        # iterate over all points in the i/p list
        for x, y in points:
            # calculate the distance from the origin
            dist = (x ** 2) + (y ** 2)
            # append the distance and the point to the minHeap
            minHeap.append([dist, x, y])
        
        # sort the minHeap list using heapify
        heapq.heapify(minHeap)

        # iterate over the minHeap list
        while k > 0:
            # pop the point with least distance from the minHeap
            dist, x, y = heapq.heappop(minHeap)
            # append the point to the `res` list
            res.append([x, y])
            # decrement the value of k
            k -= 1

        # return the `res` list
        return res

