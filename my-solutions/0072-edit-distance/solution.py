class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n,m = len(word1),len(word2)
        prev = [i for i in range(m+1)]

        for i in range(1,n+1):
            curr = [i] + [0] * m
            for j in range(1,m+1):
                if word1[i-1] == word2[j-1]:
                    curr[j] = prev[j-1]
                else:
                    curr[j] = min(prev[j-1],prev[j],curr[j-1])+1
            prev = curr
        return prev[-1]

