class Solution(object):
    def minimumMountainRemovals(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        # 왼쪽에서 증가하는 부분 수열의 길이
        left = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    left[i] = max(left[i], left[j] + 1)

        # 오른쪽에서 감소하는 부분 수열의 길이
        right = [1] * n
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if nums[i] > nums[j]:
                    right[i] = max(right[i], right[j] + 1)

        # 가장 긴 산 모양 배열의 길이 찾기
        max_mountain_len = 0
        for i in range(1, n - 1):
            if left[i] > 1 and right[i] > 1:
                max_mountain_len = max(max_mountain_len, left[i] + right[i] - 1)

        # 제거해야 하는 최소 요소 수 계산
        return n - max_mountain_len
