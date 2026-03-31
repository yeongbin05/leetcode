class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        ans = [0] * (n + m - 1)

        # T 먼저 강제로 박기
        for i in range(n):
            if str1[i] == 'T':
                for j in range(m):
                    if ans[i + j] == 0 or ans[i + j] == str2[j]:
                        ans[i + j] = str2[j]
                    else:
                        return ""

        def check_finished_f(pos):
            # pos를 끝으로 하는 F 윈도우들만 검사
            for start in range(max(0, pos - m + 1), min(n - 1, pos) + 1):
                if str1[start] == 'F' and start + m - 1 == pos:
                    same = True
                    for j in range(m):
                        if ans[start + j] != str2[j]:
                            same = False
                            break
                    if same:
                        return False
            return True

        def dfs(idx):
            if idx == n + m - 1:
                return True

            # 이미 정해진 문자면 그대로 진행
            if ans[idx] != 0:
                if check_finished_f(idx) == False:
                    return False
                return dfs(idx + 1)

            # a ~ z 넣어보기
            for k in range(26):
                ans[idx] = chr(97 + k)

                if check_finished_f(idx):
                    if dfs(idx + 1):
                        return True

                ans[idx] = 0

            return False

        if dfs(0):
            return ''.join(ans)
        return ""
