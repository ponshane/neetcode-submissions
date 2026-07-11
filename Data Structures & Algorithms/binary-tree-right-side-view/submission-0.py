# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        
        right_size_view = []
        stack = deque([root])
        
        while stack:
            size_at_layer = len(stack)

            for _ in range(size_at_layer):
                
                node = stack.popleft()
                
                # if the right-most node, we append the node's val to right_size_view
                if _ == size_at_layer-1:
                    right_size_view.append(node.val)

                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
                
        return right_size_view