'''
Question: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        Use DFS
        TC: O(log n)
        SC: O(n)
        '''
        # root will never be NULL until we find the result, a way to keep the loop running
        while root:
            # Since a BST, if both `p` and `q` are greater than current `root`
            # then `p` and `q` will ALWAYS be in the right subTree of `root`
            if p.val > root.val and q.val > root.val:
                root = root.right

            # Since a BST, if both `p` and `q` are less than current `root`
            # then `p` and `q` will ALWAYS be in the left subTree of `root`
            elif p.val < root.val and q.val < root.val:
                root = root.left

            # Since a BST, if `p` < `root` and `q` > `root` (or vice-versa)
            # then, that `root` will be LCA since there is a split (one will
            # be in the left subTree and the other in the right subTree)
            else:
                return root
            
        