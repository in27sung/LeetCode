class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        distinct_count = len(set(nums))
        count = defaultdict(int)
        res = 0
        right = 0

        for left in range(n):
            if left > 0:
                prev = nums[left - 1]
                count[prev] -= 1
                if count[prev] == 0:
                    del count[prev]
            while right < n and len(count) < distinct_count:
                count[nums[right]] += 1
                right += 1
            if len(count) == distinct_count:
                res += n - right + 1

        return res
