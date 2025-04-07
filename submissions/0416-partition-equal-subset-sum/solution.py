class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        # If total sum is odd, it can't be split into two equal subsets
        if total % 2 != 0:
            return False

        target = total // 2

        # Dynamic programming array: dp[i] indicates whether sum i is achievable
        dp = [False] * (target + 1)
        dp[0] = True  # Base case: zero sum is always achievable

        for num in nums:
            # Traverse backwards to avoid reusing the same number
            for i in range(target, num - 1, -1):
                dp[i] |= dp[i - num]

        return dp[target]
