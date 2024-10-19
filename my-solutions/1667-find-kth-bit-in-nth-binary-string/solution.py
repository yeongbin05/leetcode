class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s1 = "0"
        for i in range(n-1):
            
            temp = s1 + "1" +  ''.join(['0' if char == '1' else '1' for char in s1])[::-1]
            s1 = temp

        return s1[k-1]

