class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            digit = n & 1
            ans = (ans << 1) | digit
            n = n >> 1
        
        return ans
