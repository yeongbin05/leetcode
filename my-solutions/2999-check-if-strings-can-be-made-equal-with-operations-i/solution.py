class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        # for i in range(4):
        #     if i == 0 or i == 1:
        #         if s1[i] != s2[i]:
        #             if s1[i+2] == s2[i] and s1[i] == s2[i+1]:
        #                 continue
        #             else:
        #                 return False

        #     else:
        #         if s1[i] != s2[i]:
        #             return False
        alpha_s1 , alpha_s2 = set(),set()
        for i in range(2):
            alpha_s1.add(s1[i])
            alpha_s1.add(s1[i+2])
            alpha_s2.add(s2[i])
            alpha_s2.add(s2[i+2])
            if alpha_s1 != alpha_s2:
                return False
            alpha_s1 , alpha_s2 = set(),set()
        return True
