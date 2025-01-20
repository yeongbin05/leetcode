class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        # 값의 위치를 기록하는 딕셔너리 생성
        position = {}
        for i in range(m):
            for j in range(n):
                position[mat[i][j]] = (i, j)
        
        # 각 행과 열의 채워진 셀 개수를 기록
        row = [0] * m
        col = [0] * n
        
        # arr를 순회하며 값을 처리
        for i, val in enumerate(arr):
            if val in position:
                y, x = position[val]
                row[y] += 1
                col[x] += 1
                # 행 또는 열이 전부 채워졌는지 확인
                if row[y] == n or col[x] == m:
                    return i
