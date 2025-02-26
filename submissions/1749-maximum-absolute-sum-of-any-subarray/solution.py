class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        # Variables to track the max and min subarray sums
        max_sum = 0  # Maximum subarray sum
        min_sum = 0  # Minimum subarray sum
        current_max = 0  # Current max sum at each step
        current_min = 0  # Current min sum at each step

        for num in nums:
            # Update the current max sum considering the current element 
            current_max = max(current_max + num, num)
            max_sum = max(max_sum, current_max)

            # Update the current min sum considering the current element
            current_min = min(current_min + num, num)
            min_sum = min(min_sum, current_min)
    
        # The final answer is the maxsimum absolute value between max_sum and min_sum
        return max(abs(max_sum), abs(min_sum))

