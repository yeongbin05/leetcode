class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def canDistribute(penalty):
            # 필요한 작업 수를 계산
            operations = 0
            for balls in nums:
                if balls > penalty:
                    operations += (balls - 1) // penalty
            return operations <= maxOperations

        # 이진 탐색 범위 설정
        low, high = 1, max(nums)
        answer = high
        
        while low <= high:
            mid = (low + high) // 2
            if canDistribute(mid):  # 현재 penalty가 가능한 경우
                answer = mid
                high = mid - 1
            else:  # 현재 penalty가 불가능한 경우
                low = mid + 1
        
        return answer
