class Solution(object):
    def shortestSubarray(self, nums, k):
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        
        # 덱을 사용한 슬라이딩 윈도우
        dq = deque()
        min_length = float('inf')
        
        for i in range(n + 1):
            # 조건을 만족하는 윈도우 찾기
            while dq and prefix_sum[i] - prefix_sum[dq[0]] >= k:
                min_length = min(min_length, i - dq.popleft())
            
            # 덱의 불필요한 값 제거
            while dq and prefix_sum[i] <= prefix_sum[dq[-1]]:
                dq.pop()
            
            # 현재 인덱스를 덱에 추가
            dq.append(i)
        
        return min_length if min_length != float('inf') else -1
