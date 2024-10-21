'''
Question: https://leetcode.com/problems/invert-binary-tree
'''

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        Use Recursion
        '''
        # base case for recursion
        if root is None:
            return None

        # swap the left and right children of the node
        temp = root.left
        root.left = root.right
        root.right = temp

        # recursively call left child of the node
        self.invertTree(root.left)
        # recursively call right child of the node
        self.invertTree(root.right)

        return root
        