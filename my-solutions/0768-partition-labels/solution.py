class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        dic = {}
        for i in range(n):
            dic[s[i]] = i

        print(dic)
        ans = []
        temp = [0] * 26
        cnt = 0
        for i in range(n):
            cnt += 1
            if dic[s[i]] <= i:
                temp[ord(s[i])-ord('a')] = 0
                if sum(temp) == 0:
                    ans.append(cnt)
                    cnt = 0
            else:
                temp[ord(s[i])-ord('a')] = 1
        return ans
