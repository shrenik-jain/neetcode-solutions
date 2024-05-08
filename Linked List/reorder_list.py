'''
Question: https://leetcode.com/problems/reorder-list/
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        '''
        Part 1: 
        Find the middle of the linked list using two pointers 
        `slow` and `fast`

        Part 2:
        Reverse the second half using `reverse linked list` logic

        Part 3: 
        Merge the first half and second half (reversed) together, 
        joining nodes alternately 
                
        TC: O(n)
        SC: O(1)
        '''
        ### Consider Eg: 1->2->3->4->5->None

        ## Part 1:
        # init two pointers `slow` and `fast`
        slow, fast = head, head.next

        # while the `fast` pointer doesn't reach the end of the LL
        while fast and fast.next:
            # move `slow` pointer to the next node
            slow = slow.next
            # move `fast` pointer two nodes ahead
            fast = fast.next.next

        # After Part 1
        # Eg: 1 -> 2 -> 3 -> 4 -> 5 -> None
        #              slow            fast

        # `slow` pointer is at the center of the LL
        # so init `second` as the head of the second half of LL
        second = slow.next

        # since we have divided the list into two halves, end the first half with None
        slow.next = None
        # init `prev` as None (required for reversing the second half)
        prev = None

        # Eg: 1 -> 2 -> 3 -> None          4 -> 5 -> None
        #                  slow.next     second           


        # while `second` does not reach the end i.e. None
        while second:
            # store the next node of `second` in tmp since we will be breaking 
            # this link
            tmp = second.next
            # reverse the link by assigning `second` node to `prev`
            second.next = prev
            # now move the `prev` pointer to `second` 
            prev = second
            # and `second` pointer to its original next i.e `tmp`
            second = tmp

        first, second = head, prev

        # After Part 2
        #   1 -> 2 -> 3 -> None        None <- 4 <- 5 
        # first                                   second

        # since second half will always be shorter than first half
        while second:
            # assign actual nexts of `first` and `second` in temp vars
            # since we will break these links
            tmp1, tmp2 = first.next, second.next
            # connect first node to the last node
            first.next = second
            # connect last node to first's next node
            second.next = tmp1
            # move `first` and `second` to thier original nexts
            first, second = tmp1, tmp2

        