class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        min_price = float('inf')

        for i in prices:
            if i - min_price > ans :
                ans = i - min_price
            if i < min_price:
                min_price = i

        return ans

