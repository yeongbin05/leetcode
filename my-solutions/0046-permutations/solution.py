class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # ans = []
        # temp = []
        # def dfs(index):
        #     if len(temp) == len(nums):
                
        #         ans.append(temp.copy())
        #         return 
        #     for i in range(len(nums)):
        #         if nums[i] not in temp:
        #             temp.append(nums[i])
        #         else :
        #             continue
        #         dfs(index+1)
        #         temp.pop()

        # dfs(0)
        
        # return ans
        ans = []
        
        def dfs(path):
            if len(path) == len(nums):
                ans.append(path)
                return 
            
            for num in nums:
                if num not in path:
                    dfs(path + [num])

        dfs([])
        return ans
