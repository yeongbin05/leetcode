class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        
        dic = {}  # 문자 위치 저장
        left = 0  # 현재 부분 문자열의 시작 위치
        ans = 0   # 최장 길이 저장
        
        for right in range(n):
            if s[right] in dic:
                left = max(left, dic[s[right]] + 1)  # left를 뒤로 이동
            
            dic[s[right]] = right  # 현재 문자 위치 갱신
            ans = max(ans, right - left + 1)  # 최장 길이 갱신
        
        return ans

