class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, num in enumerate(nums):
            key = target - num
            if key in dic:
                return [dic[key], i]
            dic[num] = i
