class Solution(object):
    def minSwaps(self, nums):
        total_ones = sum(nums)
    
        if total_ones == 0:
            return 0
        
        # Step 2: Create the sliding window over a concatenated version of nums to simulate circular array
        n = len(nums)
        extended_nums = nums + nums
        
        # Step 3: Find the maximum number of 1's in any window of size total_ones
        max_ones_in_window = 0
        current_ones_in_window = 0
        
        # Initialize the first window
        for i in range(total_ones):
            current_ones_in_window += extended_nums[i]
        
        max_ones_in_window = current_ones_in_window
        
        # Slide the window
        for i in range(total_ones, n + total_ones):
            current_ones_in_window += extended_nums[i] - extended_nums[i - total_ones]
            max_ones_in_window = max(max_ones_in_window, current_ones_in_window)
        
        # The minimum swaps needed will be the number of 0's in the best window found
        min_swaps_needed = total_ones - max_ones_in_window
        
        return min_swaps_needed

            
