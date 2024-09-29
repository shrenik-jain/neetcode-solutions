'''
Question: https://leetcode.com/problems/evaluate-reverse-polish-notation/
'''

from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
        Use a stack to store tokens from left to right, if token is an operator (+-/*),
        apply the operator on the previous two numbers in the stack, and append the res in the stack again.

        TC: O(n)
        SC: O(n)
        '''
        stack = []
        # iterate on the tokens from left to right
        for tok in tokens:
            # if `+`, simply add the previous 2 values in the stack
            if tok == "+":
                stack.append(stack.pop() + stack.pop())

            # if `-` subtract the last 2 values (in order of what they were added)
            elif tok == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)

            # if `*`, simply multiply the previous 2 values in the stack
            elif tok == "*":
                stack.append(stack.pop() * stack.pop())

            # if `/` divide the last 2 values (in order of what they were added)
            elif tok == "/":
                a, b = stack.pop(), stack.pop()
                # convert to int to follow constraint -> Division between 2 integers always truncates toward 0
                stack.append(int(b / a))
            
            # if other than an operator (a digit), simply append it to the stack
            else:
                stack.append(int(tok))

        return stack[-1]