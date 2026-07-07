class Solution:
    def sumAndMultiply(self, n: int) -> int:
        temp = 0
        multiplier = 1
        x = 0
        for i in str(n)[::-1]:
            if i != '0':
                temp += int(i) * multiplier
                x += int(i)
                multiplier *= 10
        
        return temp * x
