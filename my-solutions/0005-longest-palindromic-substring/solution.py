class Solution(object):
    def longestPalindrome(self, s):
        if len(s) == 0:
            return ""
        
        start, end = 0, 0
        
        for i in range(len(s)):
            # 홀수 길이의 팰린드롬 찾기
            len1 = self.expandAroundCenter(s, i, i)
            # 짝수 길이의 팰린드롬 찾기
            len2 = self.expandAroundCenter(s, i, i + 1)
            # 더 긴 길이를 선택합니다.
            max_len = max(len1, len2)
            
            # 현재 가장 긴 팰린드롬을 갱신합니다.
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
        
        return s[start:end + 1]

    # 메서드를 클래스 레벨로 이동
    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # while 루프에서 벗어난 이후, 팰린드롬 길이는 (right - left - 1)입니다.
        return right - left - 1

