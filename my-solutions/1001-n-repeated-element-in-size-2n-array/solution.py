class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums) // 2
        repeated_times = [0] * (10001)
        for num in nums:
            repeated_times[num] += 1
            if repeated_times[num] > 1 :    
                return num
        
        # dic = {}
        # for num in nums:
        #     if num in dic:
        #         dic[num] += 1
        #     else:
        #         dic[num] = 1

        #     if dic[num] == n :
        #         return num
