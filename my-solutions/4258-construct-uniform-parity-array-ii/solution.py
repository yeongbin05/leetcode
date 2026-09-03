class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        n = len(nums1)
        min_odd,min_even = 10**9+1,10**9+1
        for i in range(n):
            if nums1[i] % 2 == 0:
                if nums1[i] < min_even:
                    min_even = nums1[i]
            else:
                if nums1[i] < min_odd:
                    min_odd = nums1[i]

        if min_odd == (10**9 + 1) or min_even == (10**9 +1):
            return True

        else:
            if min_odd < min_even:
                return True

            return False
        
