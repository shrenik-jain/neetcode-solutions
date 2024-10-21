'''
Question: https://leetcode.com/problems/subtree-of-another-tree/
'''

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        '''
        Use DFS to check if a subtree of `root` isSameTree() as `subRoot` 

        TC: O(root * subRoot)
        '''
        # if `subRoot` is NULL, it will always be a subtree of the main tree
        if not subRoot:
            return True
        
        # if first conditon doesn't satisfy, then `subRoot` is non-NULL
        # and if main tree `root` is empty, no `subRoot` will ever be a subtree of it
        if not root:
            return False

        # check if any subtree of `root` contains `subRoot`. if yes, return True
        if self.isSameTree(root, subRoot):
            return True

        # if the node of `root` does not match with node of `subRoot`, check for
        # the left of right children of `root`
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        

    def isSameTree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        '''
        Helper function to check if `s` and `t` are the same trees.
        Refer to https://leetcode.com/problems/same-tree/ and `Trees/same_tree.py`
        '''
        if not s and not t:
            return True

        if (not s or not t) or (s.val != t.val):
            return False

        return self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)
        