'''
Question: https://leetcode.com/problems/count-good-nodes-in-binary-tree/
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        Perform DFS, passing the maxVal until that node to each dfs() call

        TC: O(n)
        """
        # dfs helper function
        def dfs(node, maxVal):
            # if node is None, no goodNodes, return 0
            if not node:
                return 0

            # goodNodes will be 1 if curr node is >= maxVal else 0
            goodNodes = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)

            # count and add the num of goodNodes in the left subtree
            goodNodes += dfs(node.left, maxVal)
            # count and add the num of goodNodes in the right subtree
            goodNodes += dfs(node.right, maxVal)

            # return the final num of goodNodes
            return goodNodes
        
        # first dfs() call, with root and root.val (can also pass -ve infinity)
        return dfs(root, root.val)