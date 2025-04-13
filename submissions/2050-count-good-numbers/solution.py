class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7  # Large prime modulus for modular arithmetic

        def mod_pow(base: int, exp: int) -> int:
            """
            Fast modular exponentiation using binary exponentiation.
            Computes (base ** exp) % MOD efficiently.
            """
            result = 1
            while exp > 0:
                if exp % 2 == 1:
                    result = (result * base) % MOD
                base = (base * base) % MOD
                exp //= 2
            return result

        # Even-indexed positions (0-based): can be filled with 0,2,4,6,8 → 5 choices
        # Odd-indexed positions: can be filled with 1,3,5,7 → 4 choices
        evens = (n + 1) // 2
        odds = n // 2

        return (mod_pow(5, evens) * mod_pow(4, odds)) % MOD
