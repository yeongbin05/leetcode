class Solution(object):
    def smallestDistancePair(self, nums, k):
        # Step 1: Sort the array
        nums.sort()
        length = len(nums)
        
        # Step 2: Initialize binary search range
        start = 0
        end = nums[-1] - nums[0]
        
        def count_pairs(mid):
            count = 0
            j = 0
            for i in range(length):
                # Move j to the point where nums[j] - nums[i] > mid
                while j < length and nums[j] - nums[i] <= mid:
                    j += 1
                count += j - i - 1
            return count
        
        # Step 3: Perform binary search
        while start < end:
            mid = (start + end) // 2
            if count_pairs(mid) >= k:
                end = mid  # Narrow down the search to the smaller half
            else:
                start = mid + 1  # Narrow down the search to the larger half
        
        # Step 4: Return the result
        return start

