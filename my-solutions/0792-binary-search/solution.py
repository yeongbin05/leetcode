class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        # if n == 1:
        #     if nums[0] == target:
        #         return 0
        #     else:
        #         return -1
        left , right = 0 , n-1
        while right >= left :
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                right = middle -1
            else:
                left = middle + 1
        

        return -1
