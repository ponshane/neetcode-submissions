# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sameTree(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        stack = [(root1, root2)]
        while stack:
            node1, node2 = stack.pop()

            if node1 == None and node2 == None:
                continue

            if not node1 or not node2 or node1.val != node2.val:
                return False
            else:
                stack.append((node1.left, node2.left))
                stack.append((node1.right, node2.right))
            
        return True

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if root == None and subRoot == None:
            return True
        
        stack = [root]

        while stack:
            node = stack.pop()

            if node.val == subRoot.val:
                if self.sameTree(node, subRoot):
                    return True

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
                
        return False
