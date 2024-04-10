'''
Question: https://leetcode.com/problems/3sum/
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        Brute Force: Run three loops to find every combination of 3 numbers that add to 0
                    Naive approach and doesn't handle duplicates 

        Optimal: sort the array and for every element, find other two numbers that add up 
                to 0. Basically Two Sum for sorted array (Two Sum II)

        Time Complexity = O(nlogn) [sorting] + O(n^2) = O(n^2)
        Space Complexity = O(n) [sorting requires extra space]
        '''
        result = []
        n = len(nums)
        nums.sort()

        for idx, curr_num in enumerate(nums):

            # since we sorted the array, and out of the three numbers, 
            # if the number in the first position is positive we are never going
            # to be able to get to a sum of 0, since all numbers after curr_num will be 
            # greater than 0 
            if curr_num > 0:
                break 

            # its the same number as previously visited, so skip it and continue to the next number
            if idx > 0 and curr_num == nums[idx-1]:
                continue

            # left pointer set to index after curr_num
            l = idx + 1
            # right pointer set to last number in nums
            r = n - 1

            # keep looping until left doesn't cross right
            while(l < r):
                threeSum = curr_num + nums[l] + nums[r]

                # number is positive so shift right pointer to a smaller number (i.e previous number)
                if threeSum > 0:
                    r -= 1
                
                # number is negative so shift left pointer to a larger number (i.e next number)
                elif threeSum < 0:
                    # Remember to move to the next number in the list
                    l += 1
                
                # found the three numbers so append to result
                else:
                    result.append([curr_num, nums[l], nums[r]])
                    l += 1

                    # we keep moving forward until the left pointer is not the same as the previous
                    # left pointer. We do this to avoid duplicates
                    while(l < r and nums[l] == nums[l-1]):
                        l += 1

        return result