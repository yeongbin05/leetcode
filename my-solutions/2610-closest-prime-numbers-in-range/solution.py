class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def find_primes(n):
            is_prime = [True] * (n + 1)
            is_prime[0] = is_prime[1] = False
            
            for i in range(2, int(n ** 0.5) + 1):
                if is_prime[i]:
                    for j in range(i * i, n + 1, i):
                        is_prime[j] = False
            
            return [i for i in range(left, n + 1) if is_prime[i]]

        primes = find_primes(right)
        
        # 소수가 2개 미만이면 [-1, -1] 반환
        if len(primes) < 2:
            return [-1, -1]
        
        # 가장 가까운 소수 쌍 찾기
        min_diff = float('inf')
        closest_pair = [-1, -1]
        
        for i in range(len(primes) - 1):
            diff = primes[i + 1] - primes[i]
            if diff < min_diff:
                min_diff = diff
                closest_pair = [primes[i], primes[i + 1]]

        return closest_pair
