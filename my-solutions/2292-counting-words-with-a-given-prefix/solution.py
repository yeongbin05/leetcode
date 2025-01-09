class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        ans = 0
        f = len(pref) 
        for i in words:
            if i[:f] == pref:
                ans += 1

        return ans
