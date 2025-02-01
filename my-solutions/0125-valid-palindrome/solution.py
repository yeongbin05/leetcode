class Solution:
    def isPalindrome(self, s: str) -> bool:
        converted = ''
        for i in s :
            if i.isalnum():
                converted += i.lower()
        return converted == converted[::-1]
