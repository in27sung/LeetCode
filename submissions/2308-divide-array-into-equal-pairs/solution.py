class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        # Count frequency of each number
        count = Counter(nums)

        # Check if all counts are even
        return all(freq % 2 == 0 for freq in count.values())
