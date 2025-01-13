class Solution:
    def minimumLength(self, s: str) -> int:
        n = len(s)
        ans = 0
        frequency = [0] * 26
        for current_char in s:
            frequency[ord(current_char) - ord("a")] += 1
        
        for fre in frequency:
            if fre == 0 :
                continue
            if fre % 2 == 0:
                ans += fre - 2
            else:
                ans += fre - 1


        return n - ans
