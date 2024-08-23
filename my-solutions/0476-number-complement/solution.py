class Solution:
    def findComplement(self, num: int) -> int:
        mask = (1 << num.bit_length()) - 1
    
        # XOR 연산을 통해 보수를 구함
        return num ^ mask
