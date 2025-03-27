class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        m = len(nums)
        dic = {}
        for i in range(m):
            if nums[i] not in dic:
                dic[nums[i]] = 1
            else:
                dic[nums[i]] += 1
        dic_left = {}
        cnt = 0
        for i in range(m):
            cnt += 1
            if nums[i] not in dic_left:
                dic_left[nums[i]] = 1
            else:
                dic_left[nums[i]] += 1
            dic[nums[i]] -= 1
            m -= 1
            if dic_left[nums[i]] > cnt//2 and dic[nums[i]] > m // 2:
                return i
        return -1

