'''
Question: https://leetcode.com/problems/min-stack/
'''

class MinStack:
    '''
    Maintain a minStack to keep track of the minimum of all the numbers in the main stack
    '''

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        # push the element in the main stack
        self.stack.append(val)
        # push the current minimum of the main stack in the `minStack`
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()