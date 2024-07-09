'''
Question: https://leetcode.com/problems/valid-parentheses/
'''

class Solution:
    def isValid(self, s: str) -> bool:
        '''
        Maintain a stack (LIFO System)
        if char is an open bracket append it to stack
        if char is a closing bracket, check if the coresponding opening bracket is at the top of the stack

        TC: O(n)
        SC: O(n)
        '''
        stack = []
        # maintain a hashmap for coresponding  bracket pairs
        closeToOpen = { ')':'(', '}':'{', ']':'[' }

        # check every bracket in string `s`
        for bracket in s:
            # if it is a closing bracket
            if bracket in closeToOpen:
                # check if stack is not empty and the bracket at the top of 
                # the stack is corresponding to the current closing bracket 
                if stack and stack[-1] == closeToOpen[bracket]:
                    # if yes, then pop that element
                    stack.pop(-1)

                # else there seems to be a mismatch of brackets
                # eg (]
                else:
                    return False
            # if it is an opening bracket, simply append it to the stack
            else:
                stack.append(bracket)

        # if at the end, the stack is empty then return True else False
        return True if not stack else False

