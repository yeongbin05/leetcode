class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        left, right = 0, len(queries)
        answer = -1
        
        # 이진 탐색 시작
        while left <= right:
            mid = (left + right) // 2
            if self.isValid(nums[:], queries, mid):
                answer = mid  # 가능한 k 값을 저장
                right = mid - 1  # 더 작은 k를 찾기 위해 줄이기
            else:
                left = mid + 1  # k를 늘려야 한다면 증가
                
        return answer

    def isValid(self, nums, queries, k):
        n = len(nums)
        diff = [0] * (n + 1)

        # 앞에서 k개의 쿼리를 적용
        for i in range(k):
            l, r, val = queries[i]
            diff[l] -= val
            if r + 1 < n:
                diff[r + 1] += val

        # 차분 배열을 원래 배열로 변환하면서 검증
        curr = 0
        for i in range(n):
            curr += diff[i]  # 누적 합을 이용해 현재 값 변경
            nums[i] += curr  # nums 배열 업데이트
            if nums[i] > 0:  # 만약 0이 안 된다면 실패
                return False
        
        return True
