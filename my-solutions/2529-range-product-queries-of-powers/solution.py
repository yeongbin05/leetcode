class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7

        # 1) n의 이진수에서 1인 비트 위치(지수)만 추출 (오름차순)
        exps = []
        i, x = 0, n
        while x:
            if x & 1:
                exps.append(i)      # powers에 들어갈 항은 2^i
            i += 1
            x >>= 1

        # 2) 지수 prefix sum
        pref = [0]
        for e in exps:
            pref.append(pref[-1] + e)

        # 3) 쿼리 처리: 곱 = 2^(지수합) mod M
        ans = []
        for l, r in queries:
            exp_sum = pref[r + 1] - pref[l]
            ans.append(pow(2, exp_sum, MOD))
        return ans

