class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        # Use a set to store unique digit arrangements of valid palindromes
        digit_patterns = set()

        # Half length to generate base for palindromes
        half_len = (n + 1) // 2
        start = 10 ** (half_len - 1)
        end = 10 ** half_len

        is_odd = n % 2

        # Generate all palindromes of length n
        for i in range(start, end):
            half = str(i)
            full = half + half[-2::-1] if is_odd else half + half[::-1]
            palin = int(full)

            if palin % k == 0:
                digit_patterns.add("".join(sorted(full)))

        # Precompute factorials up to n
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i

        result = 0

        # For each unique digit arrangement, calculate permutations avoiding leading zeros
        for digits in digit_patterns:
            count = [0] * 10
            for d in digits:
                count[int(d)] += 1

            # First digit cannot be 0 → choose any non-zero digit as first
            leading_options = n - count[0]

            # Total permutations = (n-1)! * leading options / repeated digit counts
            perm = leading_options * fact[n - 1]
            for c in count:
                perm //= fact[c]
            result += perm

        return result
