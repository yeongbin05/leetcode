# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         min_price = prices[0] 
#         dp = [0] * len(prices)
#         for i in range(1,len(prices)):
#             if prices[i] < min_price :
#                 min_price = prices[i]

#             if prices[i] > min_price :
#                 dp[i] = prices[i] - min_price
    
#         return max(dp)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0] 
        profit = 0 
        for i in range(1,len(prices)):
            min_price = min(min_price, prices[i])  # 매번 최소 가격 업데이트
            profit = max(profit, prices[i] - min_price)

        return profit
