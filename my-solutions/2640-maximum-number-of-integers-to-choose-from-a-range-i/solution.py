class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned_set = set(banned)
        
        # [1, n] 범위에서 banned에 포함되지 않은 숫자를 필터링
        nums = [i for i in range(1, n + 1) if i not in banned_set]
        
        # 작은 숫자부터 더할 수 있도록 정렬
        nums.sort()
        
        # 최대 합을 초과하지 않으면서 선택 가능한 숫자의 개수를 카운트
        current_sum = 0
        count = 0
        
        for num in nums:
            if current_sum + num > maxSum:
                break
            current_sum += num
            count += 1
        
        return count
