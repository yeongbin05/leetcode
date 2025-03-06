class Solution:
    def isHappy(self, n: int) -> bool:
        nums = set()
        while 1:
            temp = 0
            for i in str(n):
                temp += int(i)**2
            if temp == 1:
                return True
            print(nums,temp)
            if temp in nums:
                return False
            else:
                nums.add(temp)
            n = temp
