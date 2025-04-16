class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = Counter()
        left = 0
        right = -1
        pair_count = 0
        result = 0

        for left in range(n):
            # Expand the right boundary until we have at least k good pairs
            while pair_count < k and right + 1 < n:
                right += 1
                pair_count += count[nums[right]]
                count[nums[right]] += 1

            # If we have enough pairs, all subarrays [left...x] for x ∈ [right, n-1] are valid
            if pair_count >= k:
                result += n - right

            # Shrink from the left, updating the count and pair total
            count[nums[left]] -= 1
            pair_count -= count[nums[left]]

        return result
