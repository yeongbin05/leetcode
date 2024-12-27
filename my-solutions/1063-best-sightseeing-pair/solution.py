class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        ans = 0
        temp = values[0]
        for i in range(1,n):
            ans = max(ans,temp + values[i]-i)
            temp = max(temp,values[i]+i)

        return ans

