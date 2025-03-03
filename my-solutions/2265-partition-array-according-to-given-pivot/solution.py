class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        left = []
        piv = []
        right = []
        for i in range(n):
            if nums[i] < pivot:
                left.append(nums[i])
            elif nums[i] == pivot :
                piv.append(nums[i])
            else:
                right.append(nums[i])

        
        return left + piv + right
