class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7
        graph = defaultdict(list)

        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))

        distance = [float('inf')] * n
        ways = [0] * n
        distance[0] = 0
        ways[0] = 1

        heap = [(0, 0)] # (distance, node)

        while heap:
            dist_u, u = heappop(heap)
            
            if dist_u > distance[u]:
                continue

            for v, weight in graph[u]:
                continue

            for v, weight in graph[u]:
                if dist_u + weight < distance[v]:
                    distance[v] = dist_u + weight
                    ways[v] = ways[u]
                    heappush(heap, (distance[v], v))

                elif dist_u + weight == distance[v]:
                    ways[v] = (ways[v] + ways[u]) % MOD

        return ways[n - 1]

