class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        type_of_jewels = set()
        ans = 0
        for jewel in jewels:
            type_of_jewels.add(jewel)

        for stone in stones:
            if stone in type_of_jewels:
                ans += 1

        return ans
