class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        # 배열이 회전되지 않은 경우, 첫 번째 원소가 최소값입니다.
        if nums[left] < nums[right]:
            return nums[left]
        
        # 이진 탐색을 통해 최소값의 위치를 찾습니다.
        while left < right:
            mid = (left + right) // 2
            # 중간 원소가 오른쪽 원소보다 크다면, 최소값은 오른쪽 부분에 있습니다.
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        return nums[left]

