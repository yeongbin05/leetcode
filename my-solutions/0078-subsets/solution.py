class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def back(idx,temp):
            if idx == len(nums):
                ans.append(temp[:])
                return
            temp.append(nums[idx])
            back(idx+1,temp)
            temp.pop()
            back(idx+1,temp)
        
        back(0,[])
        return ans
