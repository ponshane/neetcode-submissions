class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        links = {i:[] for i in range(n)}
        for u, v in edges:
            links[u].append(v)
            links[v].append(u)
        visited = {i: False for i in range(n)}

        def bfs(node):
            queue = deque([node])
            while queue:
                node = queue.popleft()
                visited[node] = True
                for nei in links[node]:
                    if visited[nei] == False:
                        queue.append(nei)
        res = 0
        for i in range(n):
            if visited[i] == False:
                bfs(i)
                res += 1
        return res