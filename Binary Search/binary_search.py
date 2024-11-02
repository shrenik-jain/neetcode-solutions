"""
Question: https://leetcode.com/problems/binary-search    
"""

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # init two pointers at the start and end of the list
        low, high = 0, len(nums)-1

        # iterate until the two pointers meet
        while low <= high:
            # calculate the mid index
            mid = (high + low) // 2

            # if the target is found, return the index
            if target == nums[mid]:
                return mid
            
            # if the target is less than the mid element, search the left half
            elif target < nums[mid]:
                high = mid - 1

            # if the target is greater than the mid element, search the right half    
            else:
                low = mid + 1

        # if the target is not found, return -1
        return -1
        