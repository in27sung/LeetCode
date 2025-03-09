class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        """
        Find the closest prime numbers within the given range using Miller-Rabin primality test.

        Args:
            left: Lower bound of the range (inclusive)
            right: Upper bound of the range (inclusive)

        Returns:
            List containing the closest prime pair, or [-1, -1] if none exists
        """
        # Handle edge cases
        if right - left < 1:
            return [-1, -1]

        # Special case for small primes
        left = max(2, left)
        if left == 2 and right >= 3:
            return [2, 3]  # Smallest possible gap

        # Start with odd numbers (except when starting from 2)
        if left & 1 == 0:
            left += 1

        prev_prime = -1
        min_gap = float('inf')
        closest_pair = [-1, -1]

        def is_probable_composite(n: int, witness: int, d: int, s: int) -> bool:
            """
            Check if n is probably composite using a single witness.

            Args:
                n: Number to test
                witness: Base to use for the test
                d, s: Parameters where n-1 = d * 2^s

            Returns:
                True if definitely composite, False if probably prime
            """
            x = pow(witness, d, n)
            if x == 1 or x == n - 1:
                return False

            for _ in range(1, s):
                x = pow(x, 2, n)
                if x == n - 1:
                    return False
            return True

        def is_prime(n: int) -> bool:
            """
            Determine if n is prime using the Miller-Rabin primality test.
            This implementation is deterministic for n < 3,317,044,064,679,887,385,961,981

            Args:
                n: Number to test

            Returns:
                Boolean indicating whether n is prime
            """
            if n < 2:
                return False

            # Check small primes directly
            small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
            for p in small_primes:
                if n == p:
                    return True
                if n % p == 0:
                    return False

            # Decompose n-1 as d * 2^s
            s = 0
            d = n - 1
            while d & 1 == 0:
                d >>= 1
                s += 1

            # Miller-Rabin bases that are sufficient for 64-bit integers
            witnesses = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

            # Check primality with each witness
            for witness in witnesses:
                if is_probable_composite(n, witness, d, s):
                    return False
            return True

        # Main loop to find closest primes
        for candidate in range(left, right + 1, 2):
            if not is_prime(candidate):
                continue

            if prev_prime != -1:
                current_gap = candidate - prev_prime

                # Early return for minimum possible gap (twin primes)
                if current_gap == 2:
                    return [prev_prime, candidate]

                if current_gap < min_gap:
                    min_gap = current_gap
                    closest_pair = [prev_prime, candidate]

            prev_prime = candidate

        return closest_pair
