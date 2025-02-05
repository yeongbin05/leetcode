import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        left,right = 1,max(piles)

        while right > left:
            mid = (left + right) // 2
            temp = 0
            for i in piles:
                temp += math.ceil(i/mid)
            if temp <= h :
                right = mid 
            else:
                left = mid + 1

        return left
