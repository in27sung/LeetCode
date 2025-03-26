class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # Flatten the grid
        flat = [num for row in grid for num in row]
        flat.sort()
        median = flat[len(flat) // 2]

        # Check feasibility and compute total steps
        if any((num - median) % x != 0 for num in flat):
            return -1

        return sum(abs(num - median) // x for num in flat)
