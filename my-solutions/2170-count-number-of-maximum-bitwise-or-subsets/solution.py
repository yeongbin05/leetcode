class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        maximum = 0
        ans = 0
        def back(temp, idx):
            nonlocal ans
            if idx == n:  
                if temp == maximum:
                    ans += 1
                return

            # 1) 현재 nums[idx] 포함
            back(temp | nums[idx], idx + 1)
            # 2) 현재 nums[idx] 제외
            back(temp, idx + 1)

        for i in range(n):
            maximum |= nums[i]
        
        # 첫 인자 : 현재 원소까지 OR값 , 두 번째 인자 : idx값
        back(0,0)


        return ans
