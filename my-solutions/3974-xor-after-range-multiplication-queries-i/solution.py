class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        m = len(queries)
        MOD =  10**9 + 7
        for i in range(m):
            idx = queries[i][0]
            while idx <= queries[i][1]:
                nums[idx] = (nums[idx] * queries[i][3]) % (MOD)
            
                idx += queries[i][2]

        ans = nums[0]
        for i in range(1,n):
            ans ^= nums[i]
        return ans
