# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        num_good_nodes = 0
        
        stack = [(root, -101)]

        while stack:
            node, current_maximum = stack.pop()

            # decide if node is good
            if node.val >= current_maximum:
                num_good_nodes += 1
                current_maximum = node.val
            
            if node.left:
                stack.append((node.left, current_maximum))
            
            if node.right:
                stack.append((node.right, current_maximum))
        
        return num_good_nodes
            
