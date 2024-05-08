'''
Question: https://leetcode.com/problems/linked-list-cycle/
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        Keep two pointers `fast` and `slow`. `slow` moves ahead one node
        and `fast` moves ahead two nodes. If `fast` and `slow` meet at the
        same node, a cycle exists

        TC: O(n)
        SC: O(1)
        '''
        # init two pointers, both at head
        slow, fast = head, head

        # while `fast` and `fast`'s next node is not None 
        # i.e we have not arrived at the end of the linked list
        while fast and fast.next:
            # move `slow` pointer one node ahead
            slow = slow.next
            # move `fast` pointer two nodes ahead
            fast = fast.next.next

            # if `slow` and `fast` meet at the same node
            # a cycle exists
            if slow == fast:
                return True

        # both pointers did not meet, hence no cycle exists
        return False
    