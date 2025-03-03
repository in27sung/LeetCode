class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left, right = [], []
        count = 0 # Count occurrences of pivot

        for num in nums:
            if num < pivot:
                left.append(num)
            elif num > pivot:
                right.append(num)
            else:
                count += 1 # Count number of pivots
        return left + [pivot] * count + right




                
                
