class Solution:
    def minimumDeletions(self, s: str) -> int:
        # # a 인덱스 중에 max찾아서 그 보다 index작은 b 개수
        # # b 인덱스 중에 min찾아서 그 보다 index큰 a개수 
        # # 위 두개 중 min값
        # # 결과 :  틀림 
        
        # # a 위치 저장할 변수 temp
        # temp = 0 
        # length = len(s)
        # for i in range(length-1,-1,-1):
        #     if s[i] == 'a':
        #         temp = i
        #         break
        # b_count = 0
        # for j in range(temp):
        #     if s[j] == 'b' :
        #         b_count += 1
        # # b 위치 저장할 변수 temp
        # temp = 0
        # for i in range(length):
        #     if s[i] == 'b' :
        #         temp = i 
        #         break
        # a_count = 0
        # for j in range(temp+1,length):
        #     if s[j] == 'a' :
        #         a_count += 1

        # return min(a_count,b_count)
        
        b_count = 0  # 'b'의 수를 추적
        min_deletions = 0  # 최소 삭제 횟수

        for char in s:
            if char == 'b':
                b_count += 1
            else:  # char == 'a'
                # 'a'를 만났을 때, 이전의 모든 'b'를 제거하거나 현재 'a'를 제거
                min_deletions = min(min_deletions + 1, b_count)
        
        return min_deletions
