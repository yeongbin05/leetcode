class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        n = len(s1)
        s1_odd, s1_even = [],[]
        s2_odd, s2_even = [],[]
        for i in range(0,n,2):
            s1_even.append(s1[i])
            s2_even.append(s2[i])
        
        if sorted(s1_even) != sorted(s2_even):
            return False


        for i in range(1,n,2):
            s1_odd.append(s1[i])
            s2_odd.append(s2[i])
        if sorted(s1_odd) != sorted(s2_odd):
            return False

        return True
