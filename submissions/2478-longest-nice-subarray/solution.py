class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left, mask, max_len = 0, 0, 0

        for right in range(len(nums)):
            # Shrink window if there are overlapping 1-bits
            while (mask & nums[right]) != 0:
                mask ^= nums[left]  # Remove leftmost number from mask
                left += 1

            # Add current number to the mask
            mask |= nums[right]

            # Update maximum window length
            max_len = max(max_len, right - left + 1)

        return max_len
