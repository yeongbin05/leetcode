import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        dic = {}
        paragraph = re.sub(r'[!?,;.\']',' ',paragraph).lower().split()

        cnt = 0
        for i in paragraph:
            if i not in banned:
                if i in dic:
                    dic[i] += 1
                else:
                    dic[i] = 1
                if dic[i] > cnt:
                    cnt += 1
                    ans = i
        return ans
