class Solution(object):
    from collections import deque
    def longestSubarray(self, nums, limit):
        left = 0
        max_deque = deque()
        min_deque = deque()
        max_length = 0
        
        for right in range(len(nums)):
            # max_deque 유지
            while max_deque and nums[right] > max_deque[-1]:
                max_deque.pop()
            max_deque.append(nums[right])
            
            # min_deque 유지
            while min_deque and nums[right] < min_deque[-1]:
                min_deque.pop()
            min_deque.append(nums[right])
            
            # 현재 윈도우가 조건을 만족하지 않으면 왼쪽 포인터 이동
            while max_deque[0] - min_deque[0] > limit:
                if max_deque[0] == nums[left]:
                    max_deque.popleft()
                if min_deque[0] == nums[left]:
                    min_deque.popleft()
                left += 1
            
            # 조건을 만족하는 현재 윈도우의 길이 계산
            max_length = max(max_length, right - left + 1)
        
        return max_length
