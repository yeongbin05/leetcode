class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        ans = 0
        text = text.split(' ')
        for i in text:
            for j in i:
                if j in brokenLetters:
                    break
            else:
                ans += 1

        return ans
