'''
Question: https://leetcode.com/problems/clone-graph/
'''

from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        '''
        Use DFS to make copies for each node

        TC: O(n) = Num of Edges + Num of Vertices
        SC: O(n)
        '''
        # Edge Case: if the node is Null/None
        if not node:
            return None
        # to keep track of the node copies we already made
        oldToNew = {}

        def dfs(node):
            # base case: if the node copy has already been made
            if node in oldToNew:
                return oldToNew[node]

            # if above condition skips, then node copy doesn't exist, so create one
            copy = Node(node.val)
            # add the copy to hashMap to track that the copy for curr node has already been made
            oldToNew[node] = copy

            # iterate over all neighbors of the current node, and call `dfs()` for each to create copies
            for n in node.neighbors:
                # add them as neighbours of the current node `copy`
                copy.neighbors.append(dfs(n))

            # return the newly made copy node
            return copy

        # return the node, once the copy has been made
        return dfs(node)
  