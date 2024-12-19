'''
Question: [Leetcode Premium] -> https://leetcode.com/problems/graph-valid-tree
          [Neetcode Free] -> https://neetcode.io/problems/valid-tree
'''

from typing import List
from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        Approach: Perform DFS on the graph and check if all nodes are visited and there are no cycles

        Time Complexity: O(Edges + Vertices) 
        Space Complexity: O(Edges + Vertices)
        """
        # if there are no nodes, return False
        if not n:
            return False
        
        # create an adjacency list to represent the graph
        adj = defaultdict(list)
        # create a set to keep track of visited nodes
        visit = set()

        # populate the adjacency list with each node and its neighbors (undirected graph)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        def dfs(node, prev):
            """
            Helper Function: Perform DFS on the graph
            """
            # if the node is already visited (cycle exists), return False
            if node in visit:
                return False
            
            # if-block skipped, hence add the current node to the visited set
            visit.add(node)

            # go through all the neighbors of the current node
            for n in adj[node]:
                # if the neighbor is the previous node, skip it (no need to visit it again)
                if n == prev:
                    continue

                # perform DFS on the neighbor node, if it returns False, return False immediately
                if not dfs(n, node):
                    return False
            
            # if the above loop executes without returning anything, return True
            return True

        # perform DFS on the graph starting from the first node (0) and the previous node as -1 (no previous node)
        # if the DFS returns True and all nodes are visited (they are connected), return True
        return dfs(0, -1) and len(visit) == n