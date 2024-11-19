class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        dic = {}
        window_sum = 0

        # 초기 윈도우 구성
        for i in range(k):
            window_sum += nums[i]
            dic[nums[i]] = dic.get(nums[i], 0) + 1

        # 초기 중복 확인
        if len(dic) == k:
            ans = max(ans, window_sum)

        # 슬라이딩 윈도우 시작
        for i in range(k, n):
            # 윈도우 오른쪽 값 추가
            window_sum += nums[i]
            dic[nums[i]] = dic.get(nums[i], 0) + 1

            # 윈도우 왼쪽 값 제거
            window_sum -= nums[i - k]
            if dic[nums[i - k]] == 1:
                del dic[nums[i - k]]
            else:
                dic[nums[i - k]] -= 1

            # 중복 없는 경우 갱신
            if len(dic) == k:
                ans = max(ans, window_sum)

        return ans

