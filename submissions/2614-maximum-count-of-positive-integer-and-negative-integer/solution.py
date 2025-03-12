class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        positive_count = len(nums) - bisect_right(nums, 0)
        negativ_count = bisect_left(nums, 0)

        return max(positive_count, negativ_count)
