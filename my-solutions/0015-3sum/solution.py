class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            start ,end = i+1,n-1

            while end > start:
                temp = nums[i] + nums[start] + nums[end]
                if temp == 0 :
                    ans.append([nums[i], nums[start],nums[end]])
                    while start < end and nums[start] == nums[start + 1]:
                        start += 1
                    while start < end and nums[end] == nums[end - 1]:
                        end -= 1
                    
                    start += 1
                    end -= 1
                elif temp > 0 :
                    end -= 1
                else :
                    start += 1


        return ans
