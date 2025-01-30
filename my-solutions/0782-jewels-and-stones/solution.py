class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans = 0
        dic = {}
        for i in jewels:
            if i not in dic:
                dic[i] = 1

        for i in stones:
            if i in dic:
                ans += 1

        return ans 
