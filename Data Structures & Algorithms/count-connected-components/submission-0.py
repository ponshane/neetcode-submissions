class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        visit = set()
        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(cur):
            if cur in visit:
                return
            
            visit.add(cur)
            for nei in adj[cur]:
                dfs(nei)
        
        n_components = 0
        for cur in range(n):
            if cur not in visit:
                dfs(cur)
                n_components += 1
        return n_components

        
