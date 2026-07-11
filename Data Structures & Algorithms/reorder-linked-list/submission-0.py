# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        # apply slow and fast to find mid index
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # define the second half
        second = slow.next
        # critical!
        slow.next = None

        # reverse the second half
        prev = None
        while second:
            tmp = second.next # original next
            second.next = prev # replace next with prev
            prev = second
            second = tmp
        
        # merge two list; note that prev is the new start of reversed second half
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
