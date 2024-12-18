'''
Question: https://leetcode.com/problems/valid-anagram/
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        Store characters and their respective counts of both strings in different hashmaps and check if count
        corresponding characters have same count (or even if the character exits in other dictionary) 
            
        Time Complexity: O(n)
        Space Complexity: O(n)
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

        # iterate over the keys one of the maps
        for c in counter_s:
            # check if char count in `counter_t` for a particular character is same as the char count in `counter_s`, 
            # if not strings are not anagrams. If character is not present in `counter_t` then also strings are not anagrams
            if counter_s[c] != counter_t.get(c, 0):
                return False

        return True 


        # # Another Solution
        # '''
        # iterate over sorted strings and check if both characters are same. If not same, it is not an anagram
        # 
        # Time Complexity: O(nlogn) [sorting] + O(n) = O(nlogn)
        # Space Complexity: O(1) if sorting takes no space else O(n) 
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
        