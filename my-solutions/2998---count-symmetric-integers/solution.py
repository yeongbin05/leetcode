class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0
        for i in range(low,high+1):
            i = str(i)
            Len = len(i)
            if Len % 2 == 0 and sum(int(j) for j in i[:Len//2]) == sum(int(j) for j in i) / 2:
                ans += 1
                # print(i,sum(int(j) for j in i[:Len//2]),sum(int(j) for j in i) / 2)
        
        return ans
