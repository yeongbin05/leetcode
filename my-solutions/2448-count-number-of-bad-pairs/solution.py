class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        dic = {}
        for i in range(n):
            key = i -nums[i]
            if key in dic:
                dic[key] += 1
            else:
                dic[key] = 1
        
        temp = n*(n-1) // 2

        for i in dic:
            if dic[i] >= 2:
                temp -= (dic[i]*(dic[i]-1))//2

        return temp
