class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        m = max(nums)
        divisors = [0] * (m+1)
        dic = {}
        for i in range(1,m+1):
            for j in range(i,m+1,i):
                divisors[j] += 1
                if j in dic:
                    dic[j] += [i]
                else:
                    dic[j] = [i]

        ans = 0
        for i in nums:
            if divisors[i] == 4:
                ans += sum(dic[i])
                
        return ans
