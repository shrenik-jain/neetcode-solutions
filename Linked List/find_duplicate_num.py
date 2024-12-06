'''
Question: https://leetcode.com/problems/find-the-duplicate-number/
'''

from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Floyd's Algorithm to detect cycle

        Step 1: Use slow and fast pointers to detect a cycle
        Step 2: init slow2 at the begining of the list, move slow and slow2 ahead until they meet
        Step 3: return slow or slow2

        Note: We move to the next index in this list, represented by the value
        val - [1  3  4  2  2]
        idx -  0  1  2  3  4

        0 pointing towards 1st index (3)
        3 pointing towards 3rd index (2)
        2 pointing towards 2nd index (4)
        4 pointing towards 4th index (2)

        0 -> 3 -> 2 -> 4
                  ↑    |
                  | <- ↓
        """
        # init slow and fast pointers
        slow, fast = 0, 0

        # loop until slow and fast meet
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        # init the second slow pointer
        slow2 = 0

        # loop until slow and slow2 meet
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                return slow     # or slow2
        