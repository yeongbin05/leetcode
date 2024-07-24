class Solution(object):
    def sortJumbled(self, mapping, nums):
        mapped_nums = []
        for num in nums:
            mapped_str = ''.join(str(mapping[int(digit)]) for digit in str(num))
            mapped_value = int(mapped_str)
            mapped_nums.append((mapped_value, num))
        
        
        mapped_nums.sort(key=lambda x: x[0])
        
      
        sorted_nums = [num for _, num in mapped_nums]
        
        return sorted_nums
