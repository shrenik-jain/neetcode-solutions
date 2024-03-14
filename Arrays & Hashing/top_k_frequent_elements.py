'''
Question: https://leetcode.com/problems/top-k-frequent-elements/
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        Use bucket sort to store the frequency as index and numbers that occur that many 
        index-times as elements in that index

        Time Complexity: O(n)
        Space Complexity: O(n)
        '''
        #  Create a count map to store the count of each number
        count = {}
        # Freq list is used to store the count (as indexes) to the numbers with that count (list of val)
        #  Example [[], [3], [2], [1], [], [], []] i.e 3 occurs once, 2 -> twice, 1 -> thrice....
        #  The length of this array would be len(nums) + 1 i.e. indexs (0, len(nums))
        freq = [[] for i in range(len(nums) + 1)]
        res = []
        
        # Store the count of each digit in count dict 
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        # Store the num at index times it has occured (frequency)
        for key, val in count.items():
            freq[val].append(key)

        # Start from end of array and append k elements in res array
        for i in range(len(freq)-1, 0, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res
            
            