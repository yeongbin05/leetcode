from typing import List


class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        n, m = len(grid), len(grid[0])

        total = 0
        for i in range(n):
            for j in range(m):
                total += grid[i][j]

        # 1. 가로 - 위쪽 영역이 더 크거나 같은 경우 검사
        temp = 0
        dic1 = {}
        for i in range(n - 1):
            for j in range(m):
                temp += grid[i][j]
                if grid[i][j] in dic1:
                    dic1[grid[i][j]] += [[i, j]]
                else:
                    dic1[grid[i][j]] = [[i, j]]

            if temp * 2 == total:
                return True

            sub = temp - (total - temp)
            if sub > 0 and sub in dic1:
                h = i + 1
                w = m

                if h >= 2 and w >= 2:
                    return True
                elif h == 1:
                    for row, col in dic1[sub]:
                        if col == 0 or col == m - 1:
                            return True
                elif w == 1:
                    for row, col in dic1[sub]:
                        if row == 0 or row == i:
                            return True

        # 2. 가로 - 아래쪽 영역이 더 크거나 같은 경우 검사
        temp = 0
        dic1 = {}
        for i in range(n - 1, 0, -1):
            for j in range(m):
                temp += grid[i][j]
                if grid[i][j] in dic1:
                    dic1[grid[i][j]] += [[i, j]]
                else:
                    dic1[grid[i][j]] = [[i, j]]

            if temp * 2 == total:
                return True

            sub = temp - (total - temp)
            if sub > 0 and sub in dic1:
                h = n - i
                w = m

                if h >= 2 and w >= 2:
                    return True
                elif h == 1:
                    for row, col in dic1[sub]:
                        if col == 0 or col == m - 1:
                            return True
                elif w == 1:
                    for row, col in dic1[sub]:
                        if row == i or row == n - 1:
                            return True

        # 3. 세로 - 왼쪽 영역이 더 크거나 같은 경우 검사
        temp = 0
        dic2 = {}
        for j in range(m - 1):
            for i in range(n):
                temp += grid[i][j]
                if grid[i][j] in dic2:
                    dic2[grid[i][j]] += [[i, j]]
                else:
                    dic2[grid[i][j]] = [[i, j]]

            if temp * 2 == total:
                return True

            sub = temp - (total - temp)
            if sub > 0 and sub in dic2:
                h = n
                w = j + 1

                if h >= 2 and w >= 2:
                    return True
                elif h == 1:
                    for row, col in dic2[sub]:
                        if col == 0 or col == j:
                            return True
                elif w == 1:
                    for row, col in dic2[sub]:
                        if row == 0 or row == n - 1:
                            return True

        # 4. 세로 - 오른쪽 영역이 더 크거나 같은 경우 검사
        temp = 0
        dic2 = {}
        for j in range(m - 1, 0, -1):
            for i in range(n):
                temp += grid[i][j]
                if grid[i][j] in dic2:
                    dic2[grid[i][j]] += [[i, j]]
                else:
                    dic2[grid[i][j]] = [[i, j]]

            if temp * 2 == total:
                return True

            sub = temp - (total - temp)
            if sub > 0 and sub in dic2:
                h = n
                w = m - j

                if h >= 2 and w >= 2:
                    return True
                elif h == 1:
                    for row, col in dic2[sub]:
                        if col == j or col == m - 1:
                            return True
                elif w == 1:
                    for row, col in dic2[sub]:
                        if row == 0 or row == n - 1:
                            return True

        return False
