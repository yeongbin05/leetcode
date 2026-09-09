class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0
        if n < 1000:
            return 0
        elif n < 10**6:
            return n - 999


        elif n < 10 ** 9 :
            ans += (10** 6 - 10**3)
            ans += (n -  (10**6 -1)) * 2
            return ans

        elif n < 10 ** 12:
            ans += (10** 6 - 10**3)
            ans += (10**9 -  (10**6)) * 2
            ans += (n -  (10**9-1)) * 3
            return ans

        elif n < 10 ** 15:
            ans += (10** 6 - 10**3)
            ans += (10**9 -  (10**6)) * 2
            ans += (10**12 -  (10**9)) * 3
            ans += (n-  (10**12-1)) * 4
            return ans


        elif n == 10 ** 15:
            ans += (10** 6 - 10**3)
            ans += (10**9 -  (10**6)) * 2
            ans += (10**12 -  (10**9)) * 3
            ans += (10**15-1-  (10**12-1)) * 4
            ans += 5
            return ans
