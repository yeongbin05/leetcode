class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        ans = 0
        smallest,second_smallest = float('inf'),float('inf')
        for num in nums[1:]:
            if num < smallest:
                second_smallest = smallest
                smallest = num
            
            elif num < second_smallest:
                second_smallest = num
        
        ans += (nums[0] + smallest + second_smallest)
        return ans
