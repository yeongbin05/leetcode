class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0 :
            return False
        while n >= 1:
            if n == 1:
                return True
            if n % 4 == 0:
                n = n // 4
            else:
                return False

