class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_value = 0
        max_i = 0        # Tracks the maximum nums[i] seen so far
        max_diff = 0     # Tracks the maximum nums[i] - nums[j] seen so far

        for num in nums:
            # Try using the current number as nums[k]
            max_value = max(max_value, max_diff * num)

            # Update max_diff as max_i - num (i.e., try current num as nums[j])
            max_diff = max(max_diff, max_i - num)

            # Update max_i to the highest nums[i] so far
            max_i = max(max_i, num)

        return max_value
