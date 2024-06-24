class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        flip_count = 0
        flipped = [0] * n  # 플립이 일어난 위치를 저장하는 배열
        flip = 0  # 현재 위치에서의 플립 상태를 저장

        for i in range(n):
            if i >= k:
                flip ^= flipped[i - k]  # 윈도우의 시작이 플립 상태에서 벗어나므로 플립 상태를 업데이트
            
            if nums[i] == flip:  # 현재 위치의 숫자가 플립 상태와 같다면 뒤집기가 필요함
                if i + k > n:
                    return -1  # k 길이의 뒤집기를 수행할 수 없으면 -1 반환
                flip ^= 1  # 현재 위치에서 플립 상태를 바꿈
                flip_count += 1  # 플립 횟수 증가
                flipped[i] = 1  # 플립이 일어난 위치를 기록

        return flip_count
