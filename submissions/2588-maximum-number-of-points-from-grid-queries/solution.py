class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        rows, cols = len(grid), len(grid[0])
        answers = [0] * len(queries)

        # Min-heap for BFS ordered by cell value
        min_heap = [(grid[0][0], 0, 0)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Mark the starting cell as visited by setting it to 0
        grid[0][0] = 0
        reachable_cells = 0

        # Process queries in increasing order, store original indices
        for query_index, query_value in sorted(enumerate(queries), key=lambda x: x[1]):
            # Expand reachable area while top of heap is < current query value
            while min_heap and min_heap[0][0] < query_value:
                cell_value, r, c = heappop(min_heap)
                reachable_cells += 1

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != 0:
                        heappush(min_heap, (grid[nr][nc], nr, nc))
                        grid[nr][nc] = 0  # Mark as visited

            answers[query_index] = reachable_cells

        return answers
