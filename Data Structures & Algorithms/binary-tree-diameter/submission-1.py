# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        stack = [root]
        # map only needs to store the height of each node
        height_map = {None: 0}
        max_diameter = 0

        while stack:
            node = stack[-1]

            # Post-order traversal logic:
            # If children exist and haven't been processed, go deeper
            if node.left and node.left not in height_map:
                stack.append(node.left)
            elif node.right and node.right not in height_map:
                stack.append(node.right)
            else:
                # Both children are processed (or None), now process the current node
                node = stack.pop()
                
                left_h = height_map[node.left]
                right_h = height_map[node.right]
                
                # Update global maximum using the "bridge" logic
                max_diameter = max(max_diameter, left_h + right_h)
                
                # Store height for this node so its parent can use it
                height_map[node] = 1 + max(left_h, right_h)

        return max_diameter