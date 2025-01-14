class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        dic = {}
        ans = []
        for i in range(n):
            if A[i] in dic:
                dic[A[i]] += 1
            
            else:
                dic[A[i]] = 1
            if B[i] in dic:
                dic[B[i]] += 1
            
            else:
                dic[B[i]] = 1
            temp = 0
            for j in dic:
                if dic[j] == 2 :
                    temp += 1
            
            ans.append(temp)

        return ans
