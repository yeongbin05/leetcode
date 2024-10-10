class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        # sort_nums = sorted([[i,j] for i,j in enumerate(nums)],key = lambda x: x[1])

        # min_index = 50001
        # ramp = 0
        # for i in range(len(sort_nums)):
        #     min_index = min(min_index, sort_nums[i][0])
        #     ramp = max(ramp, sort_nums[i][0] - min_index)


        # return ramp
        stack = []
        # Step 1: Build a stack of decreasing indices.
        for i in range(len(nums)):
            if not stack or nums[stack[-1]] > nums[i]:
                stack.append(i)
        
        # Step 2: Find the maximum width ramp.
        ramp = 0
        for j in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[j]:
                ramp = max(ramp, j - stack.pop())
        
        return ramp
