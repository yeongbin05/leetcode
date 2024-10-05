class Solution(object):
    def checkInclusion(self, s1, s2):
        len_s1 = len(s1)
        len_s2 = len(s2)

        if len_s1 > len_s2:
            return False
        
        # s1의 문자 빈도수를 저장하는 딕셔너리 생성
        dic1 = {}
        for i in s1:
            dic1[i] = dic1.get(i, 0) + 1
        
        # s2에서 슬라이딩 윈도우 초기화
        dic2 = {}
        for i in range(len_s1):
            dic2[s2[i]] = dic2.get(s2[i], 0) + 1
        
        # 윈도우를 하나씩 옮기면서 비교
        for i in range(len_s2 - len_s1):
            if dic1 == dic2:
                return True
            # 윈도우의 왼쪽 문자 제거
            dic2[s2[i]] -= 1
            if dic2[s2[i]] == 0:
                del dic2[s2[i]]
            # 윈도우의 오른쪽 문자 추가
            dic2[s2[i + len_s1]] = dic2.get(s2[i + len_s1], 0) + 1
        
        # 마지막 윈도우 체크
        return dic1 == dic2

