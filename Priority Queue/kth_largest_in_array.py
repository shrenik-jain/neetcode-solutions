"""
Question: https://leetcode.com/problems/kth-largest-element-in-an-array/
"""


import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        Create a MaxHeap

        TC: O(n + klogn)    O(n) => Heapify
                            O(klogn) => Removing k elements from the heap
        SC: O(n)
        '''
        # create a maxHeap, by multiplying nums with -1
        maxHeap = [-1 * n for n in nums]
        # heapify the maxHeap (sort it)
        heapq.heapify(maxHeap)

        # remove k-1 elements from the heap, so that the top element will be kth largest 
        while k > 1:
            heapq.heappop(maxHeap)
            k -= 1

        return -1 * maxHeap[0]        

    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     '''
    #     Use Quick Select Algo

    #     TC Avg  : O(n)
    #     TC Worst: O(n^2)
    #     SC      : O(1)
    #     '''
    #     # we have to find the kth largest element
    #     k = len(nums) - k

    #     def quickSelect(l, r):
    #         '''
    #         Helper quick select function
    #         '''
    #         # keep `pivot` as the rightmost element of the array we are using (based on l and r)
    #         # pointer `p` will be at the left pointer
    #         pivot, p = nums[r], l

    #         # iterate in the portion between left and right pointers
    #         for i in range(l, r):
    #             # if current element is less than pivot (rightmost element)
    #             if nums[i] < pivot:
    #                 # swap it with pointer `p`
    #                 p, nums[i] = nums[i], p
    #                 # increment pointer `p` to the next location
    #                 p += 1

    #         # finally swap the pointer `p` and pivot (rightmost element)
    #         nums[p], nums[r] = nums[r], nums[p]

    #         # if the kth largest element index is less than pointer `p` index, find in the left half
    #         if k < p:
    #             return quickSelect(l, p-1)
    #         # if the kth largest element index is greater than pointer `p` index, find in the right half
    #         elif k > p:
    #             return quickSelect(p+1, r)
    #         # if the kth largest element index is same as the pointer `p` index, we found the element
    #         else:
    #             return nums[p]

    #     # start quick select with the entire array
    #     return quickSelect(0, len(nums)-1)