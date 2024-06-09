class Solution(object):
    def subarraysDivByK(self, nums, k):
        remainder_count = {0: 1}
        current_sum = 0
        result = 0
        
        for num in nums:
            current_sum += num
            remainder = current_sum % k
            if remainder < 0:
                remainder += k  # Handle negative remainders
            
            if remainder in remainder_count:
                result += remainder_count[remainder]
                remainder_count[remainder] += 1
            else:
                remainder_count[remainder] = 1
        
        return result
