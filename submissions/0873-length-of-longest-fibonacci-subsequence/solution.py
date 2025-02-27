class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        arr_set = set(arr)  # Set for fast lookup
        longest_subseq_length = 0  # Track the longest subsequence length
        
        # Iterate over pairs of elements in arr
        for i in range(n):
            for j in range(i + 1, n):
                a, b = arr[i], arr[j]  # First two numbers of the sequence
                subseq_length = 2  # Starting length of subsequence

                # Check if the next number in the sequence exists
                while a + b in arr_set:
                    a, b = b, a + b  # Update to next Fibonacci-like pair
                    subseq_length += 1  # Increment subsequence length

                # Update the maximum subsequence length
                longest_subseq_length = max(longest_subseq_length, subseq_length)

        # Return the length if it's at least 3, else 0
        return longest_subseq_length if longest_subseq_length >= 3 else 0
