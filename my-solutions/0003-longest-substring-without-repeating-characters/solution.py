class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        cnt = {}
        ans,left,right = 0,0,0

        while right < n:
            if s[right] not in cnt:
                cnt[s[right]] = right
                right += 1
                
            else:
                left = max(left,cnt[s[right]] + 1)
                cnt[s[right]] = right
                right += 1
            ans = max(ans,right - left)

        return ans



