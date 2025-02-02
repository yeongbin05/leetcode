class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float('inf')
        ans = 0
        for i in prices:
            if i < buy :
                buy = i
            if i - buy > ans :
                ans = i - buy

        return ans
