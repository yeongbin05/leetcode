class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check(left,right):
            while 0<=left and right<n and s[left] == s[right]:
                left -=1
                right += 1
            return s[left+1:right]
        n = len(s)
        if s == s[::-1]:
            return s
        
        ans = ""
        for i in range(n-1):
            ans = max(ans,check(i,i+1),check(i,i+2),key=len)

        return ans
