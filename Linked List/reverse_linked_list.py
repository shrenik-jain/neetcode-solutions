'''
Question: https://leetcode.com/problems/reverse-linked-list/
'''

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
           
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Use Three Pointers `previous`, `current` and `temp` to store
        previous node, current node and next node respectively.
        Keep reversing the links between `current` and `previous` nodes

        TC: O(n)
        SC: O(1)
        '''
        # Init `current` pointer to head and `previous` pointer to None
        current, previous = head, None

        # while current is still a node (i.e. current != None)
        while current:
            # temporarily store the next node of `current` in `temp` var
            # this is done because `current` will point to `previous` node 
            # and the link will be broken, hence to move to the next node after 
            # reversing, we will use `temp` node
            temp = current.next
            # point current to previous node (reverse the link)
            current.next = previous
            # point previous to current node (Get ready for next reversal)
            previous = current
            # move current to next node (Get ready for next reversal)
            current = temp

        # finally return the head of the reversed list
        return previous
        