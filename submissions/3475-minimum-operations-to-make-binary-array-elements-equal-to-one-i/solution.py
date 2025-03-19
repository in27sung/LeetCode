class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        
        # Iterate through array starting from index 2
        for i in range(2, n):
            if nums[i - 2] == 0:
                count += 1
                # Flip nums[i-2], nums[i-1], nums[i]
                for j in range(i - 2, i + 1):
                    nums[j] ^= 1
        
        # Check if all elements are 1
        return count if all(num == 1 for num in nums) else -1
