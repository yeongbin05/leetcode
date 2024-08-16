class Solution(object):
    def maxDistance(self, arrays):
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        
        # Initialize the maximum distance as 0
        max_distance = 0
        
        # Iterate over the arrays starting from the second array
        for i in range(1, len(arrays)):
            # Calculate the possible distances and update the maximum distance
            max_distance = max(max_distance, abs(arrays[i][-1] - min_val), abs(max_val - arrays[i][0]))
            
            # Update the min_val and max_val for the next iteration
            min_val = min(min_val, arrays[i][0])
            max_val = max(max_val, arrays[i][-1])
        
        return max_distance
            
