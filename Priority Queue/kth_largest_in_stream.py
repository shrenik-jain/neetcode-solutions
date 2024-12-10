'''
Question: https://leetcode.com/problems/kth-largest-element-in-a-stream/
'''

from typing import List
import heapq

class KthLargest:
    '''
    Use a min heap to store only k elements in it, and return the top element

    Time Complexity: O(nlogk) for the constructor and O(logk) for the add method
    Space Complexity: O(k)
    '''

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        # do heapify (make nums a min Heap [smallest element at the top])
        heapq.heapify(self.minHeap)

        # only keep k elements in the heap, pop everything else
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
    def add(self, val: int) -> int:
        # push the new val in the heap
        heapq.heappush(self.minHeap, val)
        # only if there are greater than k elements in the heap -> POP
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
        # always return the top element of the heap (since we have only store `k` elements, the topmost 
        # value will always be the kth largest value)
        return self.minHeap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)