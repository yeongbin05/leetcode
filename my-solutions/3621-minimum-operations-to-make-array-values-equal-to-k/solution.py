class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        for i in nums:
            if i < k :
                return -1
        dic = {}
        for i in nums:
            if i > k and i not in dic:
                dic[i] = 1

        return len(dic)
