'''
Question: https://leetcode.com/problems/copy-list-with-random-pointer/
'''


from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        '''
        Make 2 Passes
        First Pass: Create deep copy of each node, and map old node to new node in a HashMap
        Second Pass: Use the hashmap to map copy node's next and random pointers to point to the 
                     same nodes as in the original

        TC: O(N)
        SC: O(N)
        '''

        # init a hashMap, and map None to None as an edge case (when the node is Null) 
        oldToCopy = {None: None}

        # FIRST PASS
        cur = head
        while cur:
            # create a deep copy of current node
            copy = Node(cur.val)
            # map old (cur) node to new (copy) node
            oldToCopy[cur] = copy
            # move cur to next pointer
            cur = cur.next

        # SECOND PASS
        cur = head
        while cur:
            # get the copy node from hashMap
            copy = oldToCopy[cur]
            # add the next link of the copy node from the hasMap
            copy.next = oldToCopy[cur.next]
            # add the random link of the copy node from the hasMap
            copy.random = oldToCopy[cur.random]
            # move cur to next pointer
            cur = cur.next

        # return the head of the deep copy node
        return oldToCopy[head]
