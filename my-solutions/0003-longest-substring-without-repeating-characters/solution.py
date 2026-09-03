class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ch = {}
        left,right = 0,0
        ans = 0
        while right < n :
            if s[right] not in ch:
                ch[s[right]] = right
                right += 1

            
            else : 

                left = max(ch[s[right]]+1,left)
                ch[s[right]] = right
                right += 1
            ans = max(ans,right-left)


        return ans
