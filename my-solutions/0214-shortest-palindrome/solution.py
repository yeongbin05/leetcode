class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        
        rev_s = s[::-1]
        combined = s + "#" + rev_s
        n = len(combined)
        lps = [0] * n  # Longest Prefix Suffix array

        # Build the LPS array
        for i in range(1, n):
            length = lps[i-1]
            while length > 0 and combined[i] != combined[length]:
                length = lps[length-1]
            if combined[i] == combined[length]:
                length += 1
            lps[i] = length

        # The number of characters to add is len(s) - lps[-1]
        add_length = len(s) - lps[-1]
        add_str = rev_s[:add_length]
        return add_str + s

