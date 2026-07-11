# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True

        if not root:
            return False

        if self.sameTree(root, subRoot):
            return True

        return (self.isSubtree(root.left, subRoot) or
        self.isSubtree(root.right, subRoot))

    
    def sameTree(self, root, subroot):
        # both are None
        if not root and not subroot:
            return True
        
        # both are valid node and have the same value
        # we recursively check their children
        if root and subroot and root.val == subroot.val:
            return (self.sameTree(root.left, subroot.left) and
            self.sameTree(root.right, subroot.right))
        
        # one of root/subroot is None and one of root/subroot is a valid node
        return False
