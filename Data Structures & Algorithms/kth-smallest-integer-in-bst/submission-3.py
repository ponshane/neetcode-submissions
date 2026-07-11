# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # iterative in-order travel implementation
        stack = []
        curr = root
        cnt = 0

        while stack or curr:
            # go left first
            while curr:
                stack.append(curr)
                curr = curr.left
            
            node = stack.pop()
            cnt += 1
            if cnt == k:
                return node.val
                
            curr = node.right