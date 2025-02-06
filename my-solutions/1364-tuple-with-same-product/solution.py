class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        ans = 0
        dic = {}
        for i in nums:
            for j in nums:
                if i != j:
                    key = i * j
                    if key in dic:
                        dic[key] += 1
                    else:
                        dic[key] = 1

        for i in dic:
            if dic[i] >= 4:
                ans += (dic[i] * (dic[i] - 2))
        return ans
