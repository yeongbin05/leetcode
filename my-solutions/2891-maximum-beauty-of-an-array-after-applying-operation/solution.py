class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        start = 0
        end = 0
        ans = 0
        temp = 0
        while 1 :
            if nums[end] - nums[start] <= k * 2:
                end += 1
                temp += 1
                if temp > ans :
                    ans = temp
            else :
                start += 1
                temp -= 1
            if start > end or end >= n :
                break
        return ans
