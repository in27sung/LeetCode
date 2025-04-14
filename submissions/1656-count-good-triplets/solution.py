class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        count = 0
        prefix = [0] * 1001  # prefix[i] = count of numbers ≤ i

        for j in range(n):
            for k in range(j + 1, n):
                # Check condition between j and k
                if abs(arr[j] - arr[k]) <= b:
                    # Determine valid range for arr[i] (i < j)
                    left = max(0, arr[j] - a, arr[k] - c)
                    right = min(1000, arr[j] + a, arr[k] + c)

                    if left <= right:
                        # Count how many arr[i] (i < j) fall into the valid range
                        count += prefix[right] - (prefix[left - 1] if left > 0 else 0)

            # Update prefix sum with arr[j]
            for i in range(arr[j], 1001):
                prefix[i] += 1

        return count
