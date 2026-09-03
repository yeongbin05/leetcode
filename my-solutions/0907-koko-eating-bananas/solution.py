import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
       left ,right = 1, max(piles)
       n = len(piles)
       while right > left:
        mid = (left+right )// 2
        temp = 0
        for i in range(n):
            temp += math.ceil(piles[i] / mid)
        if temp > h:
            left = mid + 1
        elif temp <= h :
            right = mid
        
       return left

