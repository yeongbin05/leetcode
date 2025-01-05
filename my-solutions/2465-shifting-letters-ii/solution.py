class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)  # 문자열 길이
        arr = [0] * (n + 1)  # 차분 배열 생성
        
        # 차분 배열에 이동 작업 반영
        for start, end, direction in shifts:
            shift = 1 if direction == 1 else -1
            arr[start] += shift
            arr[end + 1] -= shift
        
        # 차분 배열로 누적합 계산
        for i in range(1, n):
            arr[i] += arr[i - 1]
        
        # 각 문자 이동
        result = []
        for i in range(n):
            shift = arr[i] % 26  # 이동량이 알파벳 범위를 초과하지 않도록 처리
            new_char = chr((ord(s[i]) - ord('a') + shift) % 26 + ord('a'))
            result.append(new_char)
        
        return ''.join(result)
