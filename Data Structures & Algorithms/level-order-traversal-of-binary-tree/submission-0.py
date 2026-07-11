# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        nested_values = []
        stack = deque([root])

        while stack:
            
            size_layer = len(stack)

            # initialize list for current layer
            layer_values = []
            for _ in range(size_layer):
                node = stack.popleft()
                # append value
                layer_values.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            
            nested_values.append(layer_values)
        
        return nested_values