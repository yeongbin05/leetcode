class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        cnt = {0:-1}
        temp = 0
        ans = 0
        for idx,val in enumerate(nums):
            if val == 0 :
                temp -= 1
            else:
                temp += 1
            if temp in cnt:
                ans = max(ans,idx-cnt[temp])
            else:
                cnt[temp] = idx
        
        return ans
