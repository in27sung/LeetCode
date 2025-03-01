class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        # Apply the transformation rule for consercutive equal elements
        for i in range(len(nums) - 1): # Exclude the last element to avoid out-of-bounds access
            if nums[i] == nums[i + 1] and nums[i] != 0:
                nums[i] *= 2 # Double the first element 
                nums[i + 1] = 0 # Set the second element to zero 

        # Move all non-zero elements to the front and append zeros at the end
        return [num for num in nums if num != 0] + [0] * nums.count(0)
