class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Build adjacency list for an undirected graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node: int):
            """Recursive DFS to mark all nodes in the current component."""
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        components = 0

        # Iterate through each node
        for node in range(n):
            # Start DFS if the node hasn't been visited yet
            if node not in visited:
                dfs(node)
                components += 1  # One connected component found

        return components
