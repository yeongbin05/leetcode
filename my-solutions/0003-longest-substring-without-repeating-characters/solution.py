class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        start = 0
        ans = 0
        
        for i in range(len(s)):
            if s[i] in dic:
                start = max(start,dic[s[i]] + 1)
            
            dic[s[i]] = i

            ans = max(ans,i-start + 1)            
    
        return ans
