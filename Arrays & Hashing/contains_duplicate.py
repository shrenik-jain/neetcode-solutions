'''
Question: https://leetcode.com/problems/contains-duplicate/description/

Time Complexity: O(n)
Space Complexity: O(n)
'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''
        create a dictionary to store only unique numbers. If number occurs again, it contains duplicate
        '''
        # create a dictionary to store unique numbers as keys
        count_dict = {}

        for num in nums:
            # if number already in dictionary, return True
            if num in count_dict:
                return True
            # if number occurs first time, store it in dictionary
            else:
                count_dict[num] = 1

        return False
    
        
        # # Another Solution
        # '''
        # create a set and check its length with original list, if different then contains duplicate
        # since set only stores unique values
        # '''
        # return len(nums) != len(set(nums))
        