# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        if not p and q:
            return False
        
        if p and not q:
            return False
        
        stack = [(p, q)]
        # iterative dfs
        while stack:
            p, q = stack.pop()

            # when both p and q are none
            if not p and not q:
                continue

            # when either p or q is none OR p and q have different values
            if not p or not q or p.val != q.val:
                return False

            stack.append((p.left, q.left))
            stack.append((p.right, q.right))

        return True
            
