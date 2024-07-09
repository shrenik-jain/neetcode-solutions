'''
Question: https://leetcode.com/problems/merge-k-sorted-lists/
'''

from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''
        Use Merge Sort Algorithm to sort the K linked lists
        Use Merge Two Linked Lists Solutions to merge base case

        TC: O(nLogk)
        SC: O(n)
        '''
        # Hnadle the edge case
        if not lists or len(lists) == 0:
            return None

        # keep merging until we only have 1 LL in the list (which will be the soln)
        while len(lists) > 1:
            # create a temp list to store the two newly merged LL
            mergedList = []

            # iterate over all the LL's in `lists`
            # Be sure to skip alternate LL's since we will combine 2 Lists
            for i in range(0, len(lists), 2):
                # First LL is `i`
                l1 = lists[i]
               # Second is `i+1` or else `None` if we are at the end of the `lists`
                l2 = lists[i+1] if i+1 < len(lists) else None
                
                # append the newly merged list from `l1` and `l2` into `mergedLists`
                mergedList.append(self.mergeTwoLists(l1, l2))

            # Before: lists = [[l1], [l2], [l3], [l4]]

            # update lists with the newly merged lists
            lists = mergedList

            # After: lists = [[l1, l2], [l3], [l4]]

        # Return the first list which now contains all the lists merged
        return lists[0]


     # Helper function to merge two linked lists    
    def mergeTwoLists(self, l1, l2):
        # Done before, so refer https://leetcode.com/problems/merge-two-sorted-lists/

        dummy = ListNode()
        result = dummy
        
        while l1 and l2:
            
            if l1.val < l2.val:
                result.next = l1
                l1 = l1.next
            
            else:
                result.next = l2
                l2 = l2.next
            
            result = result.next
        
        if l1:
            result.next = l1
        elif l2:
            result.next = l2
            
        return dummy.next

        