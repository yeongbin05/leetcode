class Solution:
    def minWindow(self, s: str, t: str) -> str:
        needed = {}
        for i in t:
            if i in needed:
                needed[i]+= 1
            else:
                needed[i]=1
        left = right = 0
        start = 0 # 최소 윈도우 시작 값
        window = {}
        # 필요한 문자 개수
        valid = 0
        min_len = float('inf')
        while right < len(s):
            cur_val = s[right]
            # 현재 문자가 t에 있으면
            if cur_val in needed:
                if cur_val in window:
                    window[cur_val] += 1
                else:
                    window[cur_val] = 1
            

            # 현재 문자열의 개수로 t의 해당 문자열 개수가 충족됐을 경우
            if cur_val in window and window[cur_val] == needed[cur_val]:
                valid += 1

            while valid == len(needed):
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    # 최소 문자열 후보의 좌측 인덱스 값
                    start = left
                
                removed_char = s[left]
                left += 1
                
                # 필요한 문자 개수보다 적어졌을 때
                if removed_char in window:
                    window[removed_char] -= 1
                    if window[removed_char] < needed.get(removed_char, 0):
                        valid -= 1
            right += 1
        return s[start:start+min_len] if min_len != float('inf') else ""
