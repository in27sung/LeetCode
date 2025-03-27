class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        # Find the dominant candiate
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        total = nums.count(candidate) # Total occurrence of candidate 
        # Check valid splits
        left_count = 0 
        for i in range(len(nums) - 1):
            if nums[i] == candidate:
                left_count += 1

            left_len = i + 1
            right_len = len(nums) - left_len
            right_count = total - left_count

            if left_count > left_len // 2 and right_count > right_len // 2:
                return i
        return -1


