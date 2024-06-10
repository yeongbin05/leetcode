class Solution(object):
    def heightChecker(self, heights):
        ordered = sorted(heights)
        ans = 0
        for i in range(len(heights)):
            if heights[i] != ordered[i] :
                ans +=1
        
        return ans
