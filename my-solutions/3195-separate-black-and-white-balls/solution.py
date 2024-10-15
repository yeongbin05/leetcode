class Solution(object):
    def minimumSteps(self, s):
        # len_s = len(s)
        # ans = 0
        # end = len_s - 1

        # # 현재 문자열을 리스트로 변환 (필요하지 않으므로 제거 가능)
        # s = list(s)

        # # 끝에서부터 순회하며 검은 공('1')을 찾고, 이동할 때의 거리 계산
        # for i in range(len_s - 1, -1, -1):
        #     if s[i] == '1':
        #         ans += end - i
        #         end -= 1

        # return ans
        swap = 0
        res = 0

        for i in s:
            if i =='1':
                swap+= 1
            else:
                res += swap
            
        return res
