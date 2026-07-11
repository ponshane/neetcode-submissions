# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        first, second = head, dummy
        
        # first move first index n steps
        for _ in range(n):
            first = first.next
        
        # move both indexes until first meets None
        while first:
            first = first.next
            second = second.next
        
        # remove n node
        second.next = second.next.next

        return dummy.next


        