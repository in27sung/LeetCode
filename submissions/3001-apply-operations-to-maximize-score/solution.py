class Solution:
    MOD = 10**9 + 7

    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # Count the number of distinct prime factors for a number
        def count_prime_factors(x: int) -> int:
            count = 0
            factor = 2
            while factor * factor <= x:
                if x % factor == 0:
                    count += 1
                    while x % factor == 0:
                        x //= factor
                factor += 1
            if x > 1:
                count += 1
            return count

        prime_scores = [count_prime_factors(num) for num in nums]

        # Find previous and next dominant indices using a monotonic stack
        prev_dominant = [-1] * n
        next_dominant = [n] * n
        stack = []

        for i in range(n):
            while stack and prime_scores[stack[-1]] < prime_scores[i]:
                next_dominant[stack.pop()] = i
            if stack:
                prev_dominant[i] = stack[-1]
            stack.append(i)

        # Calculate how many subarrays each index is dominant in
        subarray_counts = [
            (i - prev_dominant[i]) * (next_dominant[i] - i) for i in range(n)
        ]

        # Build a max heap of values (using negative for min-heap simulation)
        heap = [(-nums[i], i) for i in range(n)]
        heapq.heapify(heap)

        # Fast modular exponentiation
        def mod_pow(base: int, exp: int) -> int:
            result = 1
            while exp > 0:
                if exp % 2:
                    result = (result * base) % self.MOD
                base = (base * base) % self.MOD
                exp //= 2
            return result

        score = 1
        while k > 0 and heap:
            val, i = heapq.heappop(heap)
            val = -val
            ops = min(k, subarray_counts[i])
            score = (score * mod_pow(val, ops)) % self.MOD
            k -= ops

        return score    
