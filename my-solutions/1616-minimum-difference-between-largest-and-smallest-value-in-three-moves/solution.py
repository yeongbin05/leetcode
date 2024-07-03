class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        
        nums.sort()
        n = len(nums)
        
        # Scenario 1: Three smallest changes
        scenario1 = nums[n-4] - nums[0]
        
        # Scenario 2: Two smallest and one largest change
        scenario2 = nums[n-3] - nums[1]
        
        # Scenario 3: One smallest and two largest changes
        scenario3 = nums[n-2] - nums[2]
        
        # Scenario 4: Three largest changes
        scenario4 = nums[n-1] - nums[3]
        
        # Minimum difference among all scenarios
        return min(scenario1, scenario2, scenario3, scenario4)

