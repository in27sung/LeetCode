class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums) # Length of nums
        left, right = 0, len(queries) # Binary search range 

        # Helper function to check if nums can be zeroed within 'k' queries
        def canZero(k):
            # Simulates applying the first 'k' queries and checks if nums becomes zero
            delta = [0] * (n + 1) # Difference array
            curr = nums[:] # Coply of original nums (to avoid modifying the input)

            # Apply the first 'k' queries
            for i in range(k):
                li, ri, vali = queries[i]
                delta[li] -= vali # Decrease the range start
                delta[ri + 1] += vali # Stop reducing after index ri

            # Apply the dirrerence array to compute final nums state
            curr_decrement = 0 # Running sum for applying the effect of delta
            for i in range(n):
                curr_decrement += delta[i] # Accumulate delta values
                curr[i] += curr_decrement # Apply to nums
                if curr[i] > 0: # If any value remian non-zero, k is too small
                    return False 

            return True # All values are zero

        # Perform binary search to find the smallest 'k'
        while left < right:
            mid = (left + right) // 2 # Middle value of the search space
            if canZero(mid):
                right = mid # Try smaller k
            else:
                left = mid + 1 # Increase k

        # Final check: if left queries can mkae nums zero, return left; otherwise, return -1
        return left if canZero(left) else -1


