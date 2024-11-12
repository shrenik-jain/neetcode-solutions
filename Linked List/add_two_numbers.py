'''
Question: https://leetcode.com/problems/add-two-numbers/
'''

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Simple elementary math
        
        TC: O(n)
        """
        # dummy node to store the result
        dummy = ListNode()
        # point current pointer to dummy node
        curr = dummy
        # init carry
        carry = 0
        
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # add the nodes
            val = v1 + v2 + carry
            # get carry (10's digit)
            carry = val // 10
            # get val (unit's digit)
            val = val % 10

            curr.next = ListNode(val)

            # update pointers
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
            