class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len_s,len_t = len(s),len(t)
        if len_s != len_t :
            return False
        dic_s = {}
        dic_t = {}
        for i in range(len_s):
            if s[i] in dic_s:
                dic_s[s[i]] += 1
            else:
                dic_s[s[i]] = 1
            if t[i] in dic_t:
                dic_t[t[i]] += 1
            else:
                dic_t[t[i]] = 1
        
        if dic_s == dic_t :
            return True

        else:
            return False
