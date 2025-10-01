class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = 0
        emptyBottles = 0
        while 1:
            ans += numBottles
            emptyBottles += numBottles
            if emptyBottles < numExchange:
                return ans
            numBottles = emptyBottles//numExchange
            emptyBottles -= numExchange*(emptyBottles//numExchange)

