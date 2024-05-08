'''
Question: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
'''

class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        Use Binary Search Algorithm
        '''
        # set two pointers at the start and end of `nums`
        start, end = 0, len(nums) - 1
        # init `minNum` to infinity since we have to find minimum
        minNum = float('inf')

        # while both pointer do not cross each other
        while (start <= end):
            # Edge Case: If we encounter a sorted array from `start` to `end`
            # we simply need to check the minimum number in nums (nums[start])
            # with existing minNum and return the lower number out of the two
            if nums[start] < nums[end]:
                return min(minNum, nums[start])

            # if not, find the mid index
            mid = (start + end) // 2
            # check if number at mid index is the smallest number
            minNum = min(minNum, nums[mid])

            # if number at `mid` is greater or equal than number at `start`
            # then the smaller number is bound to be at right side of mid index
            #     s     m        e
            # eg  4, 5, 6, 1, 2, 3
            if nums[mid] >= nums[start]:
                start = mid + 1

            # vice versa
            # now the minimum value is bound to be on the left side of mid index
            #     s     m        e   
            # eg  6, 1, 2, 3, 4, 5
            else:
                end = mid - 1

        return minNum
