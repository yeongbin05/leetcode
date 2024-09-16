class Solution(object):
    def findMinDifference(self, timePoints):
        # 시간을 분으로 변환하는 함수
        def toMinutes(t):
            h, m = map(int, t.split(':'))
            return h * 60 + m
        
        # 모든 시간을 분으로 변환 후 정렬
        minutes = sorted([toMinutes(t) for t in timePoints])

        # 최소 차이를 매우 큰 값으로 초기화
        min_diff = float('inf')
        
        # 인접한 시간 간의 차이를 계산
        for i in range(1, len(minutes)):
            min_diff = min(min_diff, minutes[i] - minutes[i - 1])
        
        # 마지막 시간과 첫 번째 시간의 차이(하루 순환 고려)
        min_diff = min(min_diff, (minutes[0] + 1440) - minutes[-1])

        return min_diff

