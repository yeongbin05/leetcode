class Solution(object):
    def minOperations(self, nums, k):
        total_xor = 0
        for num in nums:
            total_xor ^= num
        
        # Step 2: If total_xor is already equal to k, return 0
        if total_xor == k:
            return 0
        
        # Step 3: Find out which bits are different between total_xor and k
        diff_bits = total_xor ^ k
        
        # Step 4: Count the number of set bits in diff_bits
        operations = 0
        while diff_bits:
            operations += diff_bits & 1
            diff_bits >>= 1
        
        # Step 5: Return the count
        return operations

