class Solution(object):
    def longestValidParentheses(self, s):
        # stack = [-1]  # 스택에 초기값으로 -1을 넣어 인덱스를 맞춥니다.
        # max_length = 0

        # for i, char in enumerate(s):
        #     if char == '(':
        #         stack.append(i)
        #     else:
        #         stack.pop()  # 짝이 맞는 '('을 제거합니다.
        #         if not stack:
        #             stack.append(i)  # 스택이 비었다면 현재 위치를 추가합니다.
        #         else:
        #             max_length = max(max_length, i - stack[-1])

        # return max_length
        n = len(s)
        dp = [0] * n
        max_length = 0

        for i in range(1, n):
            if s[i] == ')':
                if s[i - 1] == '(':  # "()" 형태
                    dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
                elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '(':  # "(...)" 형태
                    dp[i] = dp[i - 1] + (dp[i - dp[i - 1] - 2] if i - dp[i - 1] >= 2 else 0) + 2
                max_length = max(max_length, dp[i])

        return max_length

