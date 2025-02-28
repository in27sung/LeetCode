class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}  # {number: index}, stores indices of encountered numbers

        for index, num in enumerate(nums):
            complement = target - num  # Number needed to reach the target
            
            if complement in index_map:
                return [index_map[complement], index]  # Found the pair
            
            index_map[num] = index  # Store the index of the current number

        # No valid pair found
        return []  

