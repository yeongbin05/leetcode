class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        num = [0] * 2**n
        for i in nums:
            num[int(i,2)] += 1

        for i in range(len(num)):
            if num[i] == 0:
                return bin(i)[2:].zfill(n)
