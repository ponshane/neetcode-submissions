"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        copydict = {}
        queue = deque([node])
        copydict[node] = Node(node.val)

        while queue:
            curr = queue.popleft()
            for nei in curr.neighbors:
                if nei not in copydict:
                    copydict[nei] = Node(nei.val)
                    queue.append(nei)
                copydict[curr].neighbors.append(copydict[nei])
        return copydict[node]
