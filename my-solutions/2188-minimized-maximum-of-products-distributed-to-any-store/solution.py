import math
class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        left,right = 1,max(quantities)

        while left < right :
            mid = (left + right) // 2
            stores_needed = 0

            for quantity in quantities:
                stores_needed += (quantity + mid - 1) // mid

            if stores_needed <= n:
                right = mid 
            else:
                left = mid + 1
            
        return left
