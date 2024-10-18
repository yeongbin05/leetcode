class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        for num in nums:
            max_or |= num

        # 결과를 저장할 변수입니다.
        count = 0

        # 백트래킹 함수 정의
        def backtrack(index, current_or):
            nonlocal count
            # 부분 집합의 비트 OR 값이 최대 OR 값과 같으면 카운트를 증가시킵니다.
            if current_or == max_or:
                count += 1
            
            # index부터 시작해 나머지 원소들을 백트래킹합니다.
            for i in range(index, len(nums)):
                # 현재 원소를 추가하여 다음으로 진행합니다.
                backtrack(i + 1, current_or | nums[i])

        # 백트래킹을 시작합니다.
        backtrack(0, 0)

        return count
