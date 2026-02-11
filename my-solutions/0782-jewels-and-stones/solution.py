class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_type = {}
        for jewel in jewels:
            if jewel not in jewel_type:
                jewel_type[jewel] = 1
        
        ans = 0
        for stone in stones:
            if stone in jewel_type:
                ans += 1
        
        return ans
