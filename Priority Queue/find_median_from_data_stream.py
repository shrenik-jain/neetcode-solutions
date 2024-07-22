'''
Question: https://leetcode.com/problems/find-median-from-data-stream/
'''

import heapq

class MedianFinder:
    '''
    Implement a heap 

    addNum TC: O(log n)
    finMedian TC: O(1)
    '''

    def __init__(self):
        # init a large heap (which will be a minHeap) and small heap (which will be a maxHeap) 
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        ## since Python does not allow to implement a maxHeap, we multiply the number by -1 so that it 
        ## acts like a maxHeap

        # by default we will push all `num` to small heap
        heapq.heappush(self.small, -1 * num)


        ## make sure every element in small heap <= every element in the large heap

        # if the max value of small heap is > min value of large heap
        if (self.small and self.large and (-1 * self.small[0]) > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)


        ## make sure difference between lengths of small and large heap is atmost 1
        
        # if small has more elements than large, move element from small -> large
        if len(self.small) - len(self.large) > 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # if large has more elements than small, move element from large -> small
        if len(self.large) - len(self.small) > 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        # if odd number of elements and small has one element greater than large
        if len(self.small) > len(self.large):
            return -1 * self.small[0]

        # if odd number of elements and large has one element greater than small
        if len(self.large) > len(self.small):
            return self.large[0] 

        # if event number of elements and small and large have equal number of elements
        return (-1 * self.small[0] + self.large[0]) / 2
        

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()