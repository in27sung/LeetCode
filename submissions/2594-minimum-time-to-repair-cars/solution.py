import math

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        rank_count = Counter(ranks)  # Count rank frequencies
        low, high = 1, min(ranks) * cars * cars

        while low < high:
            mid = (low + high) // 2
            total_repaired = 0

            # Only unique ranks processed, multiply by frequency
            for rank, count in rank_count.items():
                total_repaired += count * int(math.isqrt(mid // rank))

            if total_repaired >= cars:
                high = mid
            else:
                low = mid + 1

        return low
