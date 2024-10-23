class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dic = {}
        for i in jewels:
            if i not in dic:
                dic[i] = 1
        ans = 0
        for i in stones:
            if i in dic:
                ans += 1
        return ans
