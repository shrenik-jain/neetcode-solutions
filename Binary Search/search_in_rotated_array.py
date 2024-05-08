'''
Question: https://leetcode.com/problems/search-in-rotated-sorted-array/
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        Use Binary Search Algorithm
        '''

        # init two pointers to the start and end of the list
        left, right = 0, len(nums) - 1
        
        # while both pointers do not cross each other
        while left <= right:
            # fin the middle index
            mid = (left + right) // 2
            # check if the number at the middle is the target we're finding
            if nums[mid] == target:
                return mid

            # we are checking if we currently are in the left portion
            if nums[left] <= nums[mid]:

                # since the array is sorted (but rotated), we have two sorted portions
                # if the `target` is out of bounds of the left side i.e EITHER
                # 1. Greater than the right most value of LHS i.e `nums[mid]`
                # 2. Less than the left most value of LHS i.e `nums[left]`
                if target > nums[mid] or target < nums[left]:
                    # move to the RHS of the mid value
                    left = mid + 1
                
                # if the `target` is within bounds of the left side i.e BOTH
                # 1. Less than the right most value of LHS i.e `nums[mid]`
                # 2. Greater than the left most value of LHS i.e `nums[left]`
                else:
                    # check in the LHS only
                    right = mid - 1

            # we are checking if we currently are in the right portion
            else:

                # if the `target` is out of bounds of the right side i.e EITHER
                # 1. Less than the left most value of RHS i.e `nums[mid]`
                # 2. Greater than the right most value of RHS i.e `nums[right]`
                if target < nums[mid] or target > nums[right]:
                    # check in the LHS of mid value
                    right = mid - 1

                # if the `target` is within bounds of the right side i.e BOTH
                # 1. Greater than the left most value of RHS i.e `nums[mid]`
                # 2. Less than the right most value of RHS i.e `nums[right]`
                else:
                    # check in the RHS only
                    left = mid + 1

        # target not found, hence return -1
        return -1
        