'''
Question: https://leetcode.com/problems/group-anagrams/
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        Create a dict to map count of each char in string (key) to list of anagrams (value)
        Example {(1, 1, 1, 0....1): ["abcz", "zacb"]} 
        Counts are stored based on index of character i.e. a=0, b=1...z=25

        Time Complexity: O(m * n)
                        where, m = length of string (average)
                            n = number of strings in the list
        
        Space Complexity: O(n)
        '''
        ##########################
        '''
        # For input strs = ["eat","tea","tan","ate","nat","bat"]
        # Finally res will look something like this
        {
        (1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): ['eat', 'tea', 'ate'], 
        (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): ['tan', 'nat'], 
        (1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): ['bat']
        }
        '''
        # Defaultdict so that if the key does not exist, create one by default
        res = defaultdict(list)

        for s in strs:
            # Create a count array to store counts of each character from a to z
            count = [0] * 26

            for c in s:
                # Substract ASCII of c with "a" and store count of character in array in resp position
                # Example ASCII(a) = 80, 80-80=0
                #         ASCII(b) = 81, 81-80=1
                #         ASCII(z) = 105, 105-80=25
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)

        return res.values()