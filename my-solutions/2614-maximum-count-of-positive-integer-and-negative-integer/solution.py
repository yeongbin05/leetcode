class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)

        # 음수 개수 찾기
        start, end = 0, n - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] < 0:
                start = mid + 1  # 음수가 더 있을 가능성이 있으므로 오른쪽 탐색
            else:
                end = mid - 1  # 0 이상인 경우 왼쪽 탐색
        neg = start  # 음수 개수

        # 양수 개수 찾기
        start, end = 0, n - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] > 0:
                end = mid - 1  # 양수가 더 앞쪽에 있을 가능성이 있으므로 왼쪽 탐색
            else:
                start = mid + 1  # 0 이하인 경우 오른쪽 탐색
        pos = n - start  # 양수 개수

        return max(pos, neg)
