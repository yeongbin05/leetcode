class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        # 0만났는지 체크
        flag = False
        for i in s:
            if i == "0":
                flag = True
                continue
            if flag == True and i == "1":
                return False

        return True
