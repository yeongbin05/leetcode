class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def backtrack(tiles, path, used):
            if path:  # 빈 문자열이 아닐 때만 저장
                ans.add("".join(path))

            for i in range(len(tiles)):
                if used[i]:  # 이미 사용한 문자는 건너뜀
                    continue
                if i > 0 and tiles[i] == tiles[i - 1] and not used[i - 1]:  
                    continue  # 중복 제거 (이전 문자와 같으면 한 번만 사용)

                used[i] = True
                path.append(tiles[i])
                backtrack(tiles, path, used)
                path.pop()
                used[i] = False  # 백트래킹 후 원상 복구

        tiles = sorted(tiles)  # 중복 제거를 위해 정렬
        ans = set()
        used = [False] * len(tiles)  # 각 문자 사용 여부 체크
        backtrack(tiles, [], used)
        
        return len(ans)

# 테스트
sol = Solution()
print(sol.numTilePossibilities("AAB"))  

