class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def subset(idx):
            ans.append(list(temp))
            for i in range(idx,n):
                temp.append(nums[i])
                subset(i+1)
                temp.pop()


        temp = []
        ans = []
        n = len(nums)
        subset(0)
        return ans
