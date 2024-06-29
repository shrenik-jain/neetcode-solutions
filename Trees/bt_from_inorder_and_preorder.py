'''
Question: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
        Use Preorder and Inorder properties to construct a Binary Tree
        '''

        # base case -> if any of the lists is None
        if not preorder or not inorder:
            return None

        # create a node from the first element of preorder since root is always the first element in preorder traversal
        root = TreeNode(preorder[0])
        # find the index of root in inorder
        mid = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1: mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root