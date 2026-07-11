# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # classical DFS's in-oder travel
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        res = []

        def in_order_travel(node):

            if node.left:
                in_order_travel(node.left)
            
            res.append(node.val)

            if node.right:
                in_order_travel(node.right)
        
        in_order_travel(root)
        return res[k-1]
                
            