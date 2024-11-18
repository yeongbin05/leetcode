class Solution(object):
    def decrypt(self, code, k):
        # n = len(code)
        # code = code + code
        # if k > 0 :
        #     ans = []
        #     cnt = 0
        #     for i in range(n):
        #         temp = 0
        #         for j in range(1,k+1):
        #             temp += code[i+j]
        #         ans.append(temp)
        #     return ans
        # elif k == 0:
        #     return [0] * n

        # else :
        #     ans = []
        #     for i in range(n):
        #         cnt = 1
        #         temp = 0
        #         for j in range(1,-k+1):
        #             idx = i - cnt
        #             if idx  < 0 :
        #                 idx += n
        #                 temp += code[idx]
        #             else :
        #                 temp += code[idx]
        #             cnt += 1
                
        #         ans.append(temp)
        #     return ans
        n = len(code)
        if k == 0:
            return [0] * n

        ans = [0] * n
        window_sum = 0
        start, end = (1, k) if k > 0 else (k, -1)

        # 초기 윈도우 계산
        for i in range(start, end + 1):
            window_sum += code[i % n]

        # 슬라이딩 윈도우
        for i in range(n):
            ans[i] = window_sum
            # 윈도우 이동
            window_sum -= code[(i + start) % n]
            window_sum += code[(i + end + 1) % n]

        return ans
