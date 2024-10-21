'''
Question: https://leetcode.com/problems/same-tree/
'''

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
        Use DFS
        '''
        # BASE CASES
        # if both trees are null, then they are the same
        if not p and not q:
            return True

        # (if one the trees is null) OR (if both are non-null but have diff values)
        # then they are different trees
        if (not p or not q) or (p.val != q.val):
            return False

        # recursively check if left and right chidlren of both trees are the same
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
