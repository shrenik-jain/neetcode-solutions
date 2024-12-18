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
        Approach: DFS + Hash Map

        Time Complexity: O(n) = Num of Edges + Num of Vertices
        Space Complexity: O(n) = Num of Edges + Num of Vertices
        '''
        # Edge Case: if the node is None, return None
        if not node:
            return None
        # to keep track of the node copies we already made
        oldToNew = {}

        def dfs(node):
            '''
            DFS to create a copy of the graph
            '''
            # base case: if the copy of the node already exists, return it
            if node in oldToNew:
                return oldToNew[node]

            # if above condition skips, then copy of the node doesn't exist, so create one
            copy = Node(node.val)
            # add the copy to the dictionary, so that we don't make copies of the same node again
            oldToNew[node] = copy

            # iterate over all neighbors of the current node, and call `dfs()` for each 
            # neighbour to create a copy and add them to the current node's neighbours
            for n in node.neighbors:
                # add them as neighbours of the current node `copy`
                copy.neighbors.append(dfs(n))

            # return the newly made copy node
            return copy

        # return the node, once the copy has been made
        return dfs(node)
  