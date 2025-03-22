class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # Build adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        complete_count = 0

        # BFS for each component
        for node in range(n):
            if not visited[node]:
                queue = deque([node])
                visited[node] = True
                component_nodes = []

                while queue:
                    curr = queue.popleft()
                    component_nodes.append(curr)

                    for neighbor in graph[curr]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)

                # Step 3: Check if component is complete 
                k = len(component_nodes)
                is_complete = True
                for nd in component_nodes:
                    if len(graph[nd]) != k - 1:
                        is_complete = False
                        break

                if is_complete:
                    complete_count += 1

        return complete_count
