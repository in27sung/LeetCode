class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        result = prefix_sum = 0
        # Initialize counters for odd and even prefix sums
        even_count = 1  # There is one even sum initially (0 sum)
        odd_count = 0
        
        for num in arr:
            prefix_sum += num  # Update the running prefix sum
            
            # Check the parity of the prefix sum (even or odd)
            if prefix_sum % 2 == 0:  # Even prefix sum
                result += odd_count  # All previous odd prefix sums contribute to an odd sum
                even_count += 1  # Update the count of even prefix sums
            else:  # Odd prefix sum
                result += even_count  # All previous even prefix sums contribute to an odd sum
                odd_count += 1  # Update the count of odd prefix sums
                
            # Take the result modulo 10^9 + 7
            result %= MOD
        
        return result
        

        
