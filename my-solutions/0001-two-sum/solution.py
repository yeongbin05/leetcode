class Solution(object):
    def twoSum(self, nums, target):
        dic = {}

        for i,num in enumerate(nums):
            temp = target - num
            if temp in dic :
                return [dic[temp],i]
            
            dic[num] = i
