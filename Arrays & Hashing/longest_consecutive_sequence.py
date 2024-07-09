'''
Question: https://leetcode.com/problems/longest-consecutive-sequence/
'''

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        Check if a number is start of sequence (by checking if its left number (prev number) 
        [eg if 100 then check if 99 exists in a set or not] and start incrementing the number
        (say from 100-> 101, 102, 103... and check if those numbers exist in the set and keep 
        incrementing the count to find longest sequence) 

        Time Complexity: O(n)
        Space Complexity: O(n)
        '''
        # create a set of unique numbers in nums to check if prev or next number of curr number
        # exists or not 
        numSet = set(nums)
        longest = 0

        for n in nums:
            # check if the left (prev) number is not in numSet i.e the currernt number is 
            # a start of sequence
            if (n-1) not in numSet:
                # start length from here i.e init to length=0
                length = 0
                while(n + length in numSet):
                    # keep increasing length till the sequnce continues
                    length += 1

                # check if current length is the longest length of subsequnce
                longest = max(length, longest)

        return longest