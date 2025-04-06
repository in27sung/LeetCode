class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        nums.sort()
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]

            current = nums[i]
            best = []

            for j in range(i):
                if current % nums[j] == 0:
                    candidate = dfs(j)
                    if len(candidate) > len(best):
                        best = candidate

            memo[i] = best + [current]
            return memo[i]

        return max((dfs(i) for i in range(len(nums))), key=len)
