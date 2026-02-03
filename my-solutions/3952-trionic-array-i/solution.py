class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        if nums[1] < nums[0]:
            return False
        n = len(nums)
        ans = True
        # 0 -> 0<i<=p, 1 ->  p<=i<=q , 2 -> q<=i<n-1
        state = 0
        for i in range(n-1):
            if state == 0 :
                if nums[i] < nums[i+1] :
                    pass
                elif nums[i] > nums[i+1]:
                    state = 1
                else:
                    return False
            elif state == 1:
                if nums[i] > nums[i+1]:
                    pass
                elif nums[i] < nums[i+1]:
                    state = 2
                else:
                    return False
            elif state == 2:
                if nums[i] < nums[i+1] :
                    pass
                else:
                    return False

        
        if state == 2:
            return True
        else:
            return False
