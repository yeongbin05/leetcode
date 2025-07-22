class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # unique elements를 가지는 subarray중에 가장 큰 거 구하기
        left = 0
        temp = 0  # 현재 슬라이딩 윈도우의 합
        ans = 0   # 최대 합
        subarray = set()  # 현재 윈도우 내에 있는 원소들

        for i in range(len(nums)):
            while nums[i] in subarray:
                subarray.remove(nums[left])
                temp -= nums[left]
                left += 1
            subarray.add(nums[i])
            temp += nums[i]
            ans = max(ans, temp)

        return ans
