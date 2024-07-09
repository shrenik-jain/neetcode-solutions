'''
Question: https://leetcode.com/problems/two-sum/
'''

from typing import List

class Solution:
    '''
    iterate over the list and store the numbers in a dictionary. If the difference of target and 
    currrent number already present in dictionary then you have the two numbers which add up to the target

    Time Complexity: O(n)
    Space Complexity: O(n)
    '''
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a dict to store the numbers and their position 
        seen = {}
        for i, n in enumerate(nums):
            # find the difference of target and current number
            toFind = target - n
            # if the difference is already in the dict then return the two number positions
            if toFind in seen:
                return [seen[toFind], i]
            
            # keep stroing the current number as you proceed to the next number
            seen[n] = i 
