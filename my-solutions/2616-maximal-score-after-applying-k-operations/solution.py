import heapq
class Solution(object):
    def maxKelements(self, nums, k):
        nums =  [-i for i in nums]
        heapq.heapify(nums)
        ans = 0
        for i in range(k):
            ans += -nums[0]
            
            a = heapq.heappop(nums)
            heapq.heappush(nums,int(math.ceil(a/3)))
            

        return ans
