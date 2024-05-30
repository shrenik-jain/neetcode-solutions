'''
Question: https://leetcode.com/problems/binary-tree-level-order-traversal/
'''

import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        Use BFS for level order traversal

        TC: O(n)
        SC: O(n)
        '''
        # to store the final result
        result = []
        # to store the nodes levelwise (BFS)
        queue = collections.deque()
        # append (from right) the root to start with BFS algorithm
        queue.append(root)

        # while the `queue` still has nodes
        while queue:
            # to traverse nodes only in the current level
            qLen = len(queue)
            # to store nodes in the current level
            level = []

            # iterate only over nodes in the current level
            for i in range(qLen):
                # pop the node from the queue from RHS (FIFO)
                node = queue.popleft()

                # only add to level if node is non-NULL
                if node:
                    # append the current node to the current level list
                    level.append(node.val)
                    # append the left child of the current node to the queue
                    queue.append(node.left)
                    # append the right child of the current node to the queue
                    queue.append(node.right)

            # only append to result if the level has nodes in it
            if level:
                result.append(level)

        return result