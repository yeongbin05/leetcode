class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(i.lower() if i.isalnum() else '' for i in s )
        print(s)
        return s==s[::-1]
