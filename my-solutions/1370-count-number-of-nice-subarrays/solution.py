class Solution(object):
    def numberOfSubarrays(self, nums, k):
        from collections import defaultdict
        
        # Initialize variables
        count = 0
        current_odd_count = 0
        prefix_counts = defaultdict(int)
        
        # There is one way to have zero odd numbers before we start
        prefix_counts[0] = 1
        
        # Iterate through the array
        for num in nums:
            # Increment odd count if the number is odd
            if num % 2 == 1:
                current_odd_count += 1
            
            # If there have been (current_odd_count - k) odd numbers before,
            # then the current subarray ending at this position has exactly k odd numbers
            if current_odd_count - k in prefix_counts:
                count += prefix_counts[current_odd_count - k]
            
            # Update the count of prefix sums encountered
            prefix_counts[current_odd_count] += 1
        
        return count
        
