class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        result = 0
        for a in range(low, high + 1):
            if a < 100 and a % 11 == 0:
                result += 1
            if 1000 <= a < 10000:
                left = a // 1000 + a % 1000 // 100
                right = a % 100 // 10 + a % 10
                if left == right:
                    result += 1
        return result
