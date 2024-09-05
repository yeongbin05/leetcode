class Solution(object):
    def missingRolls(self, rolls, mean, n):
        m = len(rolls)
        total_sum = mean * (n + m)  # 총 필요한 주사위 합
        current_sum = sum(rolls)  # 이미 던져진 주사위들의 합
        remaining_sum = total_sum - current_sum  # 남은 주사위들의 합

        # 남은 주사위의 합이 만들 수 없는 경우 (최솟값은 1*n, 최댓값은 6*n)
        if remaining_sum < n or remaining_sum > 6 * n:
            return []

        # 남은 주사위들의 값을 채우기 위해 평균 분배
        result = [remaining_sum // n] * n
        extra = remaining_sum % n  # 남은 값을 분배해야 하는 경우

        # 남은 값들을 1씩 분배
        for i in range(extra):
            result[i] += 1

        return result
