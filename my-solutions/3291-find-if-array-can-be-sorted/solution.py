class Solution(object):
    def canSortArray(self, nums):
        if nums == sorted(nums):
            return True
        arr = [[] for _ in range(len(nums)+1)]
        cnt = 0
        temp = 0
        for i in range(len(nums)):
            if bin(nums[i]).count("1") == temp:
                arr[cnt].append(nums[i])
            else:
                cnt += 1
                arr[cnt].append(nums[i])
                temp = bin(nums[i]).count("1")
        
        ans = []
        for i in arr:
            if i != []:
                ans+=sorted(i)
            
            
        if ans == sorted(nums):

            return True
        else:
            return False
