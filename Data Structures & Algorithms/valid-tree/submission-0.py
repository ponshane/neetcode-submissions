class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if (n-1) < len(edges):
            return False
        
        adj = {i: [] for i in range(n)}
        for i, j in edges:
            # undirected edge
            adj[i].append(j)
            adj[j].append(i)

        visit = set()

        # valid tree: (1) all nodes are connected, (2) no cycle
        def dfs(cur, parent):
            
            if cur in visit:
                return False
            
            visit.add(cur)
            
            for nei in adj[cur]:
                if nei == parent:
                    continue
                if not dfs(nei, cur):
                    return False

            return True
        
        return dfs(0, -1) and n == len(visit)
