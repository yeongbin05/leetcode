class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        n,m = len(mat),len(mat[0])
        if m == k :
            return True
        res = [[0]*m for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                if i % 2 == 0:
                    res[i][j] = mat[i][(j+k)%m]
                else:
                    res[i][j] = mat[i][(j-k)%m]

        return mat == res
