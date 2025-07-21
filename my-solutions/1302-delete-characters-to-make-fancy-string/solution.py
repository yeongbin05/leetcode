class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = ""
        # 현재 문자
        current = ""
        # 연속된 문자 수
        temp = 0
        for i in s:
            if i == current :
                if temp == 2:
                    continue
                else:
                    temp += 1
                    ans += i
            else:
                current = i
                temp = 1
                ans += i
        
        return ans
