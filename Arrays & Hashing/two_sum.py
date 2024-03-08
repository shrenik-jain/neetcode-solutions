'''
Question: https://leetcode.com/problems/two-sum/

Time Complexity: O(n)
Space Complexity: O(n)
'''

class Solution:
    '''
    iterate over the list and store the numbers in a dictionary. If the difference of target and 
    currrent number already present in dictionary then you have the two numbers which add up to the target
    '''
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a dict to store the numbers and their position 
        counter = {}
        for i in range(len(nums)):
            # find the difference of target and current number
            k = target - nums[i]
            # if the difference is already in the dict then return the two number positions
            if k in counter:
                return [counter[k], i]
            
            # keep stroing the current number as you proceed to the next number
            counter[nums[i]] = i        
