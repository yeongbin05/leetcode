class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1

        for i in dic:
            if dic[i] % 2 == 1:
                return False

        return True
