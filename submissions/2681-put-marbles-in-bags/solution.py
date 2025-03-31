class Solution:
    def putMarbles(self, weights: list[int], k: int) -> int:
        if k == 1:
            return 0  # No cuts made

        pair_sums = sorted(weights[i] + weights[i + 1] for i in range(len(weights) - 1))
        return sum(pair_sums[-(k - 1):]) - sum(pair_sums[:k - 1])
