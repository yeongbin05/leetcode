class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        start = 0 
        dic = {}
        mx_cnt = 0
        ans = 0
        for end in range(n):
            if s[end] in dic:
                dic[s[end]] += 1
            else:
                dic[s[end]] = 1

            mx_cnt = max(mx_cnt,dic[s[end]])
            
            if end - start + 1 - mx_cnt > k:
                dic[s[start]] -= 1
                start += 1


            ans = max(ans,end-start + 1)

        return ans
        
