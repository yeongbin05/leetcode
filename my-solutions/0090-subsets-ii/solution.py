class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans= []
        nums.sort()
        def back(stack,idx):
            if stack not in ans:
                ans.append(stack[:])
            for i in range(idx,len(nums)):
                stack.append(nums[i])
                back(stack,i+1)
                stack.pop()

            
        back([],0)

        print(ans)
        return ans
