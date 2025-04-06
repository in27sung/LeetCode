class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        total_distance = [[0] * cols for _ in range(rows)]
        empty_land_marker = 0  # Used to track unvisited empty cells
        min_distance = float('inf')
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:  # Start BFS from each house
                    queue = deque([(r, c)])
                    steps = 0
                    min_distance = float('inf')

                    while queue:
                        steps += 1
                        for _ in range(len(queue)):
                            x, y = queue.popleft()

                            for dx, dy in directions:
                                nx, ny = x + dx, y + dy

                                # Visit only currently unvisited empty lands
                                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == empty_land_marker:
                                    grid[nx][ny] -= 1  # Mark as visited in current round
                                    total_distance[nx][ny] += steps
                                    queue.append((nx, ny))
                                    min_distance = min(min_distance, total_distance[nx][ny])

                    # Mark next BFS to look for a new 'unvisited' empty land value
                    empty_land_marker -= 1

        return -1 if min_distance == float('inf') else min_distance
