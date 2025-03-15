class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        low, high = 1, max(nums)  # Binary search range

        while low < high:
            mid = (low + high) // 2
            possible_thefts = 0
            index = 0

            # Greedy check: count how many non-adjacent houses can be robbed 
            while index < len(nums):
                if nums[index] <= mid:
                    possible_thefts += 1
                    index += 2 # Skip the next house to maintain the non-adjacent conditon
                else:
                    index += 1

                # Early exist: If we already have k thefts, break
                if possible_thefts >= k:
                    break
            
            # Adjust earch range based on feasibility check
            if possible_thefts >= k:
                high = mid # Reduce max reward as we can already steal from 'k' houses
            else:
                low = mid + 1 # Increase lower bound since 'mid' is too small

        return low



