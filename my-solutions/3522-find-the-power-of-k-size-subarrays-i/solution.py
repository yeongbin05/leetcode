class Solution(object):
    def resultsArray(self, nums, k):
        start = 0
        end = k - 1
        n = len(nums)
        ans = []
        
        for i in range(n-k+1):
            check = True
            temp = nums[i:i+k]
            for j in range(k-1):
                # print(j,i,temp)
                if temp[j+1] != temp[j] + 1:
                    check = False
                    ans.append(-1)
                    break
            else:
                ans.append(max(temp))

        return  ans
        
