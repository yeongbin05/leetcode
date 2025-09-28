class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        n  = len(nums)
        for i in range(n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    # print(nums[i],nums[j],nums[k])
                    if nums[i] < nums[j] + nums[k]:
                        return nums[i] + nums[j] + nums[k]
                    else:
                        break
                else:
                    break

        return 0
