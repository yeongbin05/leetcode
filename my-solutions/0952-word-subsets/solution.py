class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        n,m = len(words1),len(words2)
        bmax = [0] * 26
        ans = []
        for i in range(m):
            b = [0] * 26 
            for j in words2[i]:
                b[ord(j)-97] += 1
            for k in range(26):        
                bmax[k] = max(bmax[k],b[k])

        for i in range(n): 
            a_count = [0] * 26
            for char in words1[i]:  
                a_count[ord(char) - 97] += 1  

  
            is_universal = True  
            for j in range(26):  
                if a_count[j] < bmax[j]:  
                    is_universal = False
                    break
            if is_universal:
                ans.append(words1[i])

        return ans

