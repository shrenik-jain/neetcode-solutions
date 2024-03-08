'''
Question: https://leetcode.com/problems/valid-anagram/

Time Complexity: O(n)
Space Complexity: O(n)
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        Store characters and their respective counts of both strings in different hashmaps and check if count
        corresponding characters have same count (or even if the character exits in other dictionary) 
        '''
        # If length is not same then definitely not an anagram
        if len(s) != len(t):
            return False
        
        # create two maps to store char, count as keys and values respectively 
        counter_s, counter_t = {}, {}

        # iterate over strings and store char and count as keys and values respectively
        for i, j in zip(s, t):
            counter_s[i] = 1 + counter_s.get(i, 0)
            counter_t[j] = 1 + counter_t.get(j, 0)

        # iterate over one of the maps
        for key, value in counter_s.items():
            try:
                # check if char count in `counter_t` for a particular character 
                # is same as the char count in `counter_s`. If not, strings are not anagrams
                if counter_t[key] != value:
                    return False
            # if throws key error i.e. key does not exist in other map, therefore not an anagram
            except:
                return False

        return True  


        # # Another Solution
        # '''
        # iterate over sorted strings and check if both characters are same. If not same, it is not an anagram
        # '''

        # # If length is not same then definitely not an anagram
        # if len(s) != len(t):
        #     return False
        
        # # Iterate over sorted strings `s` and `t`
        # for i, j in zip(sorted(s), sorted(t)):
        #     # if characters are not same, not an anagram
        #     if i != j:
        #         return False

        # return True
        