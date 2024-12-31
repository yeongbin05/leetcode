class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        last_day = days[-1]  # 여행 마지막 날
        travel_days = set(days)  # 여행하는 날을 빠르게 체크하기 위해 집합 사용
        dp = [0] * (last_day + 1)  # dp[i]: 1일부터 i일까지의 최소 비용

        for i in range(1, last_day + 1):
            if i not in travel_days:  # 여행하지 않는 날
                dp[i] = dp[i-1]
            else:  # 여행하는 날
                dp[i] = min(
                    dp[i-1] + costs[0],            # 1일 패스
                    dp[max(0, i-7)] + costs[1],    # 7일 패스
                    dp[max(0, i-30)] + costs[2]    # 30일 패스
                )

        return dp[last_day]
