class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        min_length = n + 1
        bit_counts = [0] * 32  # 32비트 가정
        temp_or = 0
        start = 0
        
        for end in range(n):
            # nums[end]의 비트 카운트 업데이트
            for i in range(32):
                if nums[end] & (1 << i):
                    bit_counts[i] += 1
                    temp_or |= (1 << i)
            
            # 현재 윈도우의 OR 값이 k 이상인 경우
            while temp_or >= k and start <= end:
                current_length = end - start + 1
                if current_length < min_length:
                    min_length = current_length
                
                # nums[start] 제거 시 비트 카운트 업데이트
                for i in range(32):
                    if nums[start] & (1 << i):
                        bit_counts[i] -= 1
                        if bit_counts[i] == 0:
                            temp_or &= ~(1 << i)  # 해당 비트를 OR 결과에서 제거
                
                start += 1
        
        return min_length if min_length <= n else -1
