'''
Question: https://leetcode.com/problems/minimum-window-substring/
'''

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        Sliding Window with `l` and `r` pointers
        
        1. Assign two hashmaps `window` & `countT` to store the count of chars in
            1.1 In current window of string `s` (what we have)
            1.2 In the string `t` (what we need)
        
        2. Count the number of chars in string `t` (populate countT hashmap)
        
        3. Init two vars `have` and `need` to 
            3.1 `have` will track if char belongs to `t` and is exactly of the same count
            3.2 `need` keeps track of how many unique chars with exact count is in string `t`

        4. If have == need, then we have a new potential result, then
            4.1 Update the result
            4.2 Try shortening the window from the left side to try finding a shorter 
                window where have == need
        '''

        # Edge case
        if not t: 
            return ""

        # 1. Assign two hashmaps
        window, countT = {}, {}
        # init two variable to store the answers
        res, resLen = [-1, -1], float('inf')
        
        # 2. populate `countT` map with number of chars in string `t`
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        # 3. init two vars `have` and `need`
        # have = 0 (since no chars in window right now)
        # need = len(countT) (since we need those many unique chars in our res window)
        have, need = 0, len(countT)
        # left stays
        l = 0

        # right pointer keeps moving forward
        for r, right_char in enumerate(s):
            # update the count of current right_char in window map
            window[right_char] = 1 + window.get(right_char, 0)

            # if the `right_char` belongs to `t` and the count is exactly equal
            if right_char in countT and window[right_char] == countT[right_char]:
                # we have just satisfied that `right_char`'s requirement
                # increment have by 1
                have += 1

            # 4. while have and need are equal i.e all character counts are 
            #    satisfied from `t` in `s`
            while(have == need):
                # 4.1 update the result
                if r - l + 1 < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                # 4.2 pop elements from the left
                #     to fin a shorter window
                left_char = s[l]
                window[left_char] -= 1

                # if by chance we remove a char which belongs to `t` or if the 
                # count is lesser than required count for that character, we have
                # to decrement have by 1 
                if left_char in countT and window[left_char] < countT[left_char]:
                    have -= 1

                # finally move l pointer in front (shorten the window)
                l += 1

        # res will finally have the best window pointers
        left, right = res

        return s[left : right+1] if resLen != float('inf') else ""
