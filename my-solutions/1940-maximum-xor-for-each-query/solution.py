class Solution(object):
    def getMaximumXor(self, nums, maximumBit):
        max_xor = (1 << maximumBit) - 1  # 2^maximumBit - 1
    
        # nums 배열의 모든 원소의 XOR 누적합 계산
        xor_sum = 0
        for num in nums:
            xor_sum ^= num

        answer = []
        # 역순으로 쿼리를 처리합니다.
        for num in reversed(nums):
            # max_xor과 xor_sum의 XOR으로 최적의 k를 찾습니다.
            answer.append(max_xor ^ xor_sum)
            
            # XOR 누적합에서 마지막 원소를 제거 (XOR 연산으로 제거)
            xor_sum ^= num

        return answer
