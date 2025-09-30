class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        pre = nums
        next = []
        while 1:
            for i in range(n-1):
                element = pre[i] + pre[i+1]
                if element >= 10:
                    element %= 10
                next.append(element)
            pre = next
            next = []
            n -= 1
            if n == 1:
                return pre[0]

