class Solution(object):
    def minExtraChar(self, s, dictionary):
        word_set = set(dictionary)
    
        # DP 배열, 초기값은 모든 문자가 남는다고 가정
        dp = [float('inf')] * (len(s) + 1)
        dp[0] = 0  # 빈 문자열은 추가 문자가 0개
        
        # DP 실행
        for i in range(1, len(s) + 1):
            # i번째 문자까지에서의 최소 추가 문자 계산
            dp[i] = dp[i - 1] + 1  # i번째 문자를 추가 문자로 고려
            
            # j에서 i까지의 구간이 dictionary에 존재하면 추가 문자 줄일 수 있음
            for j in range(i):
                if s[j:i] in word_set:
                    dp[i] = min(dp[i], dp[j])
        
        return dp[len(s)]
