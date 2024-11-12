'''
Question: https://leetcode.com/problems/balanced-binary-tree/
'''

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        TC: O(n)
        SC: O(1)
        """

        def dfs(root):
            """
            Returns a list
            list[0]: Balanced or Not (True or False)
            list[1]: Height of the subtree
            """
            # if root is None -> it is balanced and height is 0 
            if not root:
                return [True, 0]

            # calculate the left and right subtree heights
            left = dfs(root.left)
            right = dfs(root.right)

            # balanced if (left and right subtrees are balanced) and
            # difference between the heights of left and right subtree <= 1
            balanced = (left[0] and right[0]) and (abs(left[1]-right[1]) <= 1)
            
            # calculate the height
            height = 1 + max(left[1], right[1])

            return [balanced, height]
        
        return dfs(root)[0]        