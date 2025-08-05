class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n,m = len(fruits),len(baskets)
        ans = 0
        for i in range(n):
            flag = False
            for j in range(m):
                if fruits[i] <= baskets[j]:
                    flag = True
                    baskets[j] = 0
                    break
            if flag == False:
                ans += 1
        return ans
