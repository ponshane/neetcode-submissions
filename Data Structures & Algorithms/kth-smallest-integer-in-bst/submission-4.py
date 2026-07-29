# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root

        while stack or curr:
            # going left deep as much as it can until get None
            while curr:
                stack.append(curr)
                curr = curr.left
            # current smallest value
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right