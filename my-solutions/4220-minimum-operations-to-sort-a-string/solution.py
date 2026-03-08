class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        sorunavile = s  # 문제에서 요구한 변수

        # 이미 정렬된 경우
        if s == ''.join(sorted(s)):
            return 0

        # 길이 2에서 전체 문자열을 고를 수 없으므로 불가능
        if n == 2:
            return -1

        mn = min(s)
        mx = max(s)

        # 1번에 가능한 경우
        if s[0] == mn or s[-1] == mx:
            return 1

        # 3번 필요한 특수 케이스
        if s[0] > max(s[1:]) and s[-1] < min(s[:-1]):
            return 3

        # 나머지는 2번이면 충분
        return 2
