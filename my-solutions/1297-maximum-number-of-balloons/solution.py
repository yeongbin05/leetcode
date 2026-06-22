class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = {
            'b' : 1,
            'a' : 1,
            'l' : 2,
            'o' : 2,
            'n' : 1
        }
        texts = {
            'b' : 0,
            'a' : 0,
            'l' : 0,
            'o' : 0,
            'n' : 0,
        }
        for i in text:
            if i in "balloon":
                texts[i] += 1
        ans = float('inf')

        for i in texts:
            temp = texts[i] // balloon[i]
            if temp < ans:
                ans = temp
        return ans
