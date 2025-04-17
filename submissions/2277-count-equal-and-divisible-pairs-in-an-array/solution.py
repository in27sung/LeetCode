class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        index_map = defaultdict(list)
        count = 0

        # Store indices of each number
        for idx, num in enumerate(nums):
            index_map[num].append(idx)

        # For each group of equal numbers, check index pairs
        for indices in index_map.values():
            n = len(indices)
            for i in range(n - 1):
                for j in range(i + 1, n):
                    if (indices[i] * indices[j]) % k == 0:
                        count += 1

        return count
