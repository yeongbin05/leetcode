class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        n = len(nums)
        count = 0
        
        # 이진 탐색 함수 정의
        def find_lower_bound(i, target):
            left, right = i + 1, n
            while left < right:
                mid = (left + right) // 2
                if nums[i] + nums[mid] >= target:
                    right = mid
                else:
                    left = mid + 1
            return left
        
        def find_upper_bound(i, target):
            left, right = i + 1, n
            while left < right:
                mid = (left + right) // 2
                if nums[i] + nums[mid] > target:
                    right = mid
                else:
                    left = mid + 1
            return left
        
        for i in range(n - 1):
            # lower와 upper에 맞는 범위의 시작과 끝 찾기
            j = find_lower_bound(i, lower)
            k = find_upper_bound(i, upper)
            count += k - j  # 범위 내의 쌍 개수를 더함
        
        return count
