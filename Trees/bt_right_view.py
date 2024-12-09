'''
Question: https://leetcode.com/problems/binary-tree-right-side-view/
'''

from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        Perform Level Order Traversal (BFS), and to `res` always add the right most node in the queue
        
        TC: O(n)
        """
        # init a queue for BFS. Add root for the first traversal
        q = deque([root])
        # init `res` to store the final result
        res = []

        # continue while the queue still has nodes
        while q:
            # init a var to store the rightmost node of the curr level
            rightSide = None
            # cal the len of the curr level
            qLen = len(q)

            # only iterate over the curr level (qLen)
            for _ in range(qLen):
                # get the node
                node = q.popleft()
                # if node is NOT None
                if node:
                    # init it as a potential rightmost node
                    rightSide = node
                    # Add its children inorder 
                    q.append(node.left)
                    q.append(node.right)

            # after traversal on curr level, if rightmost node is NOT None
            if rightSide:
                # add it to the result list
                res.append(rightSide.val)

        # return the final result
        return res
        