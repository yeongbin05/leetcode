class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
        ans = 0
        for i in dic:
            if i - 1 in dic:
                continue

            else:
                cnt = 1
                while i + 1 in dic:
                    cnt += 1
                    i += 1

            if cnt > ans :
                ans = cnt


        return ans
            
