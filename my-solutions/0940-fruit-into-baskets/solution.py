from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        if n <= 2:
            return n
        
        # 두 과일 종류와, 마지막 과일이 바뀐 위치를 추적
        first = fruits[0]
        second = -1
        left = 0
        max_fruits = 0

        # 마지막 과일이 연속된 구간의 시작 위치
        last_fruit = fruits[0]
        last_fruit_index = 0
        
        for right in range(n):
            curr = fruits[right]

            # 현재 과일이 두 바구니에 들어갈 수 있으면 계속 진행
            if curr == first or curr == second or second == -1:
                if second == -1 and curr != first:
                    second = curr
                # last_fruit이 바뀌면 위치 기록
                if curr != last_fruit:
                    last_fruit = curr
                    last_fruit_index = right
            else:
                # 새로운 과일이 나와서 바구니 하나를 교체해야 함
                # left를 이전 과일이 연속된 구간의 시작으로 옮김
                left = last_fruit_index
                first = fruits[left]
                second = curr
                last_fruit = curr
                last_fruit_index = right

            max_fruits = max(max_fruits, right - left + 1)

        return max_fruits

