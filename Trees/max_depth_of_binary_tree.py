'''
Question: https://leetcode.com/problems/maximum-depth-of-binary-tree/
'''

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
        Use Depth First Search (DFS)

        TC: O(n)
        SC: O(n)
        '''
        # base case if the node is null
        if root is None:
            return 0

        # Find the max between the left and right subtrees
        # 1 is added here for the current level's depth
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

#         # Init level and add the root to the deque
#         level = 0
#         q = deque([root])
        
#         # Keep going until you reach the leaf node i.e. until deque is empty
#         while q:
            
#             # Iterate through the current node
#             for i in range(len(q)):
#                 # Pop the root from the left (start)
#                 node = q.popleft()
#                 # Insert the left and right children to the right (end) of the deque
#                 if node.left:
#                     q.append(node.left)
#                 if node.right:
#                     q.append(node.right)
            
#             # Finally increment the level by 1
#             level += 1
        
#         return level
