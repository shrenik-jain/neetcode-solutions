'''
Question: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
'''

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        Use two pointers left(at start) and right(at end). Since sorted,
        perform binary search 
        '''
        # init left and right to start and end of list respectively
        left, right = 0, len(numbers) - 1
        
        # keep finding until left and right pointers do not cross
        while(left < right):
            # find current sum
            twoSum = numbers[left] + numbers[right]

            # if twoSum is smaller than target make twoSum larger
            # i.e. increment left pointer to next number
            if twoSum < target:
                left += 1

            # if twoSum is greater than target make twoSum smaller
            # i.e. decrement right pointer to previous number
            elif twoSum > target:
                right -= 1

            # found the two numbers that add up to target
            else:
                # we have to return 1-based indexes
                return [left+1, right+1] 
        