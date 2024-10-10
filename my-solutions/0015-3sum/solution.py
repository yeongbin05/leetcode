class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        len_nums = len(nums)
        for i in range(len_nums):
            if i > 0 and nums[i] == nums[i - 1]:  # 중복 건너뛰기
                continue
            start, end = i + 1, len_nums - 1
         

            while start < end:
                total = nums[i] + nums[start] + nums[end]
                
                if total < 0:
                    start += 1
                elif total > 0:
                    end -= 1
                else:
                    ans.append([nums[i], nums[start], nums[end]])
                    
                    # 중복 건너뛰기
                    while start < end and nums[start] == nums[start + 1]:
                        start += 1
                    while start < end and nums[end] == nums[end - 1]:
                        end -= 1
                    
                    start += 1
                    end -= 1


        return ans
