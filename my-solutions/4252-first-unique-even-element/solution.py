class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        indexes = {}
        for idx,num in enumerate(nums):
            if num not in indexes:
                indexes[num] = idx
            else:
                indexes[num] = -1

        print(indexes)
        for i in indexes:
            if i % 2 == 0 and indexes[i] != -1:
                return i

        return -1
