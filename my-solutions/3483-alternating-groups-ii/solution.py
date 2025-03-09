class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        for i in range(k-1):
            colors.append(colors[i])
        idx = 0
        ans = 0
        
        for i in range(1,k):
            if colors[i] == colors[i-1]:
                idx = i
                
        if idx == 0:
            ans += 1
        

        for i in range(k,n+k-1):

            if colors[i] == colors[i-1]:
                idx = i
            else:
                if idx <= i-k+1:
                    ans += 1

        return ans 

            
