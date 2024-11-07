class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        max_count = 0

        # 0 ~ 23 비트 위치를 확인합니다.
        for bit in range(24):
            count = 0
            # 각 숫자가 해당 비트에 1을 가지고 있는지 확인합니다.
            for num in candidates:
                if num & (1 << bit):
                    count += 1
            # 해당 비트 위치에서 1이 포함된 숫자의 최대 개수를 업데이트합니다.
            max_count = max(max_count, count)

        return max_count
