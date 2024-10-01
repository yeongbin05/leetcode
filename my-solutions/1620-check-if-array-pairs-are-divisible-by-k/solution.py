class Solution(object):
    def canArrange(self, arr, k):
        remainder_count = [0] * k
        
        # 나머지 계산 및 카운트
        for num in arr:
            remainder = num % k
            if remainder < 0:
                remainder += k
            remainder_count[remainder] += 1
        
        # 나머지가 0인 경우, 쌍을 이루기 위해 짝수여야 함
        if remainder_count[0] % 2 != 0:
            return False
        
        # 나머지가 k의 절반인 경우도 짝수여야 함
        for i in range(1, (k // 2) + 1):
            if remainder_count[i] != remainder_count[k - i]:
                return False
        
        return True

