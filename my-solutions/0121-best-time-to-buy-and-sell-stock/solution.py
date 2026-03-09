class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        min_price = float('inf')
        for idx,val in enumerate(prices):
            if val < min_price:
                min_price =val
            ans = max(ans,val-min_price)


        return ans
