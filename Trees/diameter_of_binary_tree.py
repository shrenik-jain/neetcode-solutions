'''
Question: https://leetcode.com/problems/diameter-of-binary-tree/
'''

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Calculate the left and right subtree heights recursively (dfs) and calculate the diameter
        """
        # need to define a member variable of class Solution to store the result
        self.largest_diameter = 0

        def height(root):
            """
            helper DFS function which returns the height of a subtree
            """
            # if root is None, return height = 0
            if not root:
                return 0

            # get the height of the left subtree
            left_height = height(root.left)
            # get the height of the right subtree
            right_height = height(root.right)
            # calculate the diameter, by adding left and right subtree heights
            diameter = left_height + right_height

            # check if current diameter is the largest ever seen
            self.largest_diameter = max(self.largest_diameter, diameter)

            # return current subtree height
            # 1 (for the current node) + max(left_height, right_height)
            return 1 + max(left_height, right_height)

        # initial dfs call
        height(root)
        # return the largest diameter of the tree
        return self.largest_diameter