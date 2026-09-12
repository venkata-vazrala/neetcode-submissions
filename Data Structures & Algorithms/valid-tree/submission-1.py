class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n - 1):
            return False
        links = {i:[] for i in range(n)}

        for i,j in edges:
            links[i].append(j)
            links[j].append(i)
        
        visited=set()
        def dfs(node,par):
            if node in visited:
                return False
            visited.add(node)
            for nei in links[node]:
                if nei == par:
                    continue
                if not dfs(nei, node):
                    return False
            return True

        
        return dfs(0,-1) and len(visited)==n

        