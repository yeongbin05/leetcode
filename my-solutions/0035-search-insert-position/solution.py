class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        start = 0
        end = n - 1
        if target > nums[-1]:
            return n
        elif target < nums[0] :
            return 0
        while end >= start :
            mid = (start + end) // 2

            if nums[mid] == target :
                return mid

            elif nums[mid] > target :
                end = mid - 1

            else :
                start = mid + 1
      
        return start
