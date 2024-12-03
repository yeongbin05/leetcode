class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = ''
        index = 0
        for i in range(len(s)):
            if i == spaces[index]:
                ans += " "
                index += 1
                if index == len(spaces):
                    index = 0
            
            ans += s[i]

        return ans
