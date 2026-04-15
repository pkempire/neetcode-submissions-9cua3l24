class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        tree = {i: [] for i in range(n)}
        if  len(edges) != n-1:
            return False

        for edge in edges:
            start,end = edge[0],edge[1]
            tree[start].append(end)
            tree[end].append(start)

        
        visited = set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbor in tree[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        dfs(0)
        return len(visited)==n        


