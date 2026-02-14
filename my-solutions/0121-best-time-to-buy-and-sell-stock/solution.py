class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        min_price = prices[0]
        ans = 0
        for idx in range(1,n):
            if prices[idx] < min_price :
                min_price = prices[idx]

            ans = max(ans,prices[idx]-min_price)

        return ans
