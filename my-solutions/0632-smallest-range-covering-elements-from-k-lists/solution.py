import heapq
class Solution(object):
    def smallestRange(self, nums):
        heap = []
        # temp에서 최대값을 저장할 변수입니다.
        current_max = float('-inf')
        
        # 각 배열의 첫 번째 원소를 temp에 저장하고, 힙에 넣습니다.
        for i in range(len(nums)):
            # (값, 해당 배열 인덱스, 배열 내의 인덱스)
            heapq.heappush(heap, (nums[i][0], i, 0))
            current_max = max(current_max, nums[i][0])
        
        # 초기 범위를 설정합니다. [min, max] 형태로 저장합니다.
        ans = [heap[0][0], current_max]
        
        while heap:
            current_min, list_index, element_index = heapq.heappop(heap)
            
            # 현재 범위를 계산하고 ans를 갱신합니다.
            if current_max - current_min < ans[1] - ans[0]:
                ans = [current_min, current_max]
            
            # 해당 배열의 다음 원소를 temp에 넣기 위해 인덱스를 증가시킵니다.
            if element_index + 1 < len(nums[list_index]):
                next_element = nums[list_index][element_index + 1]
                heapq.heappush(heap, (next_element, list_index, element_index + 1))
                current_max = max(current_max, next_element)
            else:
                # 해당 배열의 원소를 모두 사용했다면 종료합니다.
                break
        
        return ans
