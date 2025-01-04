class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)
        dic = {}
        ans = set()
        for i in s:
            if i not in dic:
                dic[i] = ''
                for j in dic:
                    if j != i:
                        dic[j] += i
            else:
                for k in dic[i]:
                    temp = i
                    temp += k
                    temp += i
                    ans.add(temp)
                for j in dic:
                    dic[j] += i
                dic[i] = i
            # print(dic,ans)
        return len(ans)
