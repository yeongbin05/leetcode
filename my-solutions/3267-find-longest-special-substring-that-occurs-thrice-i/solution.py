class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        temp = ""
        dic = {}
        for i in range(n):
            if i == 0:
                temp = s[0]
            else:
                if s[i-1] == s[i] :
                    temp += s[i]
                else : 
                    temp = s[i]
            for j in range(1,len(temp)+1):

                if temp[:j] in dic:
                    dic[temp[:j]] += 1
                else:
                    dic[temp[:j]] = 1

        ans = 0
        for i in dic :
            if dic[i] >= 3 and len(i) > ans:
                ans = len(i)
        if ans == 0 :
            return -1
        else:
            return ans
            
