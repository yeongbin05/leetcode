class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel = set(jewels)
        ans = 0
        for i in stones:
            if i in jewel:
                ans +=1 
        return ans
