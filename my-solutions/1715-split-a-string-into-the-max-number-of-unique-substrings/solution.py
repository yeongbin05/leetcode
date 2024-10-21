class Solution(object):
    def maxUniqueSplit(self, s):
        unique_set = set()
        
        def backtrack(start):
            # Base case: reached the end of the string
            if start == len(s):
                return 0
            
            max_count = 0
            # Try every possible substring starting from `start`
            for end in range(start + 1, len(s) + 1):
                substr = s[start:end]
                # If the substring is not in the set, add it and recurse
                if substr not in unique_set:
                    unique_set.add(substr)
                    # Recursively check for the next part of the string and update max_count
                    max_count = max(max_count, 1 + backtrack(end))
                    # Backtrack: remove the substring for the next iteration
                    unique_set.remove(substr)
            
            return max_count

        # Start backtracking from index 0
        return backtrack(0)
