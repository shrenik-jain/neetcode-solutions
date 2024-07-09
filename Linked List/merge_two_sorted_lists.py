'''
Question:  https://leetcode.com/problems/merge-two-sorted-lists/
'''

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Make use of the lists being already sorted .Kepp two pointers and keep 
        checking which value is lesser and append it to the new list
        '''
        # create a new dummy linked list
        dummy = ListNode()
        # point the tail to the new linked list `dummy`
        tail = dummy

        # continue while one of the linked lists exhausts
        while list1 and list2:
            # if current value of list1 <= list2
            if list1.val <= list2.val:
                # append list1 pointer to the `dummy` linked list
                tail.next = list1
                # move the pointer of list1 ahead
                list1 = list1.next
                
            # else if current list2 value is less than current list1 value
            else:
                # append list2 pointer to the `dummy` linked list
                tail.next = list2
                # move the pointer of list1 ahead
                list2 = list2.next
            
            # move the `tail` pointer to next node to store a new value
            tail = tail.next

        # if list1 still has nodes, append them as it is to `dummy`
        if list1:
            tail.next = list1
        
        # elif list2 still has nodes, append them as it is to `dummy`
        elif list2:
            tail.next = list2

        # return the new linked list
        return dummy.next
