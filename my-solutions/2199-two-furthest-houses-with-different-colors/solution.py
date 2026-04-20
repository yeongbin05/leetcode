class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        ans = 0
        n = len(colors)
        for i in range(n):
            for j in range(n-1,i,-1):
                if colors[i]!=colors[j]:
                    ans = max(ans,abs(j-i))
                    break
        
        return ans
