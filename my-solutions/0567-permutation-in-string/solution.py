class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1,len_s2 = len(s1),len(s2)
        if len_s1 > len_s2 :
            return False
        s1_cnt = [0] * 26
        s2_cnt = [0] * 26
        for i in range(len_s1):
            s1_cnt[ord(s1[i]) - ord('a')] += 1
            s2_cnt[ord(s2[i]) - ord('a')] += 1

        if s1_cnt == s2_cnt:
            return True

        for i in range(len_s2-len_s1):
            s2_cnt[ord(s2[i+len_s1])-ord('a')]+= 1
            s2_cnt[ord(s2[i])-ord('a')]-= 1
            if s1_cnt == s2_cnt:
                return True

        return False

