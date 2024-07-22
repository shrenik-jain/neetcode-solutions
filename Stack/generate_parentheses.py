'''
Question: https://leetcode.com/problems/generate-parentheses/
'''

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        RULE 1. Only add open parenthese if opened < n
        RULE 2. Only add close parenthese if closed < opened
        RULE 3. Valid ONLY IF opened == closed == n
        '''
        # define lists for storing single valid paranthese in `stack` and the result in `res`
        stack, res = [], []

        def validParanthese(opened: int, closed: int) -> None:
            '''
            Follow the above rules to generate a valid paranthese
            '''
            # RULE 3: base case
            if opened == closed == n:
                # append the valid paranthese as a string to `res`
                res.append("".join(stack))
                return

            # RULE 1
            if opened < n:
                stack.append("(")
                # since we added an opening bracket, increment opened count by 1
                validParanthese(opened + 1, closed)
                # remove the added valid paranthese from the stack after appending to res, 
                # since we are using `stack` as a global variable
                stack.pop()

            # RULE 2
            if closed < opened:
                stack.append(")")
                # since we added an closing bracket, increment closed count by 1
                validParanthese(opened, closed + 1)
                stack.pop()
            
        # initial call with 0 opened and 0 closed
        validParanthese(0, 0)
        return res
