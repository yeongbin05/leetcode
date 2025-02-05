class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        n = len(s1)
        dic1 = {}
        dic2 = {}
        for i in range(n):
            if s1[i] in dic1:
                dic1[s1[i]] += 1
            else:
                dic1[s1[i]] = 1

            if s2[i] in dic2:
                dic2[s2[i]] += 1
            else:
                dic2[s2[i]] = 1

        if dic1 != dic2 :
            return False

        cnt = 0
        for i in range(n):
            if s1[i] != s2[i] :
                cnt += 1
            
            if cnt > 2:
                return False

        if cnt != 0 and cnt != 2:
            return False
        else:
            return True
