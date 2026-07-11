# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        slow, fast = head, head

        # fast could be the first which meets null
        # AND fast moves two steps so fast.next should be not null
        while fast and fast.next:
            
            slow = slow.next # one step
            fast = fast.next.next # two step

            if slow == fast:
                return True
        
        return False

            