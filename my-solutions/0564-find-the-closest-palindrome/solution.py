class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        candidates = set()
        
        # Edge case: 1, 0, and larger lengths
        if n == '1':
            return '0'
        if n == '0':
            return '1'
        
        # Generate candidate palindromes
        prefix = n[:(length + 1) // 2]
        for i in [-1, 0, 1]:
            new_prefix = str(int(prefix) + i)
            candidates.add(self.create_palindrome(new_prefix, length))
        
        # Special cases for all 9's and 10...01 type palindromes
        candidates.add(str(10 ** (length - 1) - 1))  # 999...999
        candidates.add(str(10 ** length + 1))  # 100...001
        
        # Remove the original number if it is in the candidates
        candidates.discard(n)
        
        # Find the closest palindrome
        closest_palindrome = None
        min_diff = float('inf')
        for candidate in candidates:
            diff = abs(int(candidate) - int(n))
            if diff < min_diff or (diff == min_diff and int(candidate) < int(closest_palindrome)):
                min_diff = diff
                closest_palindrome = candidate
        
        return closest_palindrome
    
    def create_palindrome(self, s: str, length: int) -> str:
        """Creates a palindrome based on the left half 's' and length of the full number."""
        if length % 2 == 0:
            return s + s[::-1]
        else:
            return s + s[-2::-1]
