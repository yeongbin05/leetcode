class Solution:
    def maxProduct(self, n: int) -> int:
        n = str(n)
        first,second = 0,0
        for i in n:
            i = int(i)
            if i >= first:
                second = first
                first = i
            elif i > second:
                second = i

        return first * second
