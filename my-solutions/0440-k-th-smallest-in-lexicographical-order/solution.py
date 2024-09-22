class Solution(object):
    def findKthNumber(self, n, k):
        def count_steps(prefix, n):
            """현재 prefix로 시작하는 숫자들의 개수를 계산."""
            current = prefix
            next_prefix = prefix + 1
            steps = 0
            while current <= n:
                steps += min(n + 1, next_prefix) - current
                current *= 10
                next_prefix *= 10
            return steps
        
        current = 1
        k -= 1  # 첫 번째 숫자는 항상 1이므로 k를 줄임
        
        while k > 0:
            steps = count_steps(current, n)
            if steps <= k:
                # 현재 prefix의 모든 숫자를 건너뛰기
                current += 1
                k -= steps
            else:
                # 현재 prefix 안으로 들어가서 탐색
                current *= 10
                k -= 1
        
        return current

