class Solution(object):
    def minSubarray(self, nums, p):
        sum_arr = sum(nums)  
        remain = sum_arr % p  
        if remain == 0:
            return 0 
        
        dic = {0: -1}  
        prefix_sum = 0
        min_len = len(nums) 
        
        for i, num in enumerate(nums):
            prefix_sum = (prefix_sum + num) % p  
            target = (prefix_sum - remain) % p 

          
            if target in dic:
                min_len = min(min_len, i - dic[target])
            
        
            dic[prefix_sum] = i

        return min_len if min_len < len(nums) else -1  
