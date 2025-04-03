class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        result = 0
        imax = 0 # The max value of nums[i] seen so far
        dmax = 0 # The max value of nums[i] - nums[j] for i < j

        for num in nums:
            result = max(result, dmax * num) # Try nums[k] as the third element
            dmax = max(dmax, imax - num) # Try nums[j] as the middle element
            imax = max(imax, num) # Track max nums[i]
        
        return result
