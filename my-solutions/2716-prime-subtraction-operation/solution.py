from bisect import bisect_left
class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        # if len(nums) == 1:
        #     return True
        # sub = [i for i in range(2,1001)]
        
        # prime = []
        # for i in range(len(sub)):
        #     if sub[i] != 0 :
        #         prime.append(sub[i])
        #         for j in range(i,len(sub),sub[i]):
        #             sub[j] = 0
        # temp0 = 0
        # for i in prime:
        #     if i < nums[0]:
        #         temp0 = i
        #     else:
        #         break
        # nums[0] -= temp0
       
        # for i in range(1,len(nums)):
        #     temp = 0
        #     check = 1
        #     for j in prime:
        #         if j < nums[i] and nums[i] - j > nums[i-1]:
        #             temp = j
        #         else:
        #             break
        #     nums[i] -= temp
 
        #     # 순 증가인지 체크
        #     for a in range(len(nums)-1):
        #         if nums[a] >= nums[a+1]:
        #             check = 0
        #             break
        #     if check == 1:
        #         return True

       
        # return False
        valid = [True] * 1001
        valid[0] = valid[1] = False
        for i in range(2, int(len(valid) ** 0.5) + 1):
            if valid[i]:
                for j in range(i * i, len(valid), i):
                    valid[j] = False
        prime = [i for i in range(len(valid)) if valid[i]]

        temp0 = 0  # 이전 값 추적
        for num in nums:
            if num <= temp0:
                return False

            # num - temp0보다 작은 최대 소수 찾기
            idx = bisect_left(prime, num - temp0) - 1
            temp = prime[idx] if idx >= 0 else 0

            num -= temp
            temp0 = num  # temp0 업데이트

        return True
