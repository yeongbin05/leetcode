class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        temp = []
        for i in grid:
            temp += i
        temp.sort()
        n = len(temp)
        median = temp[n//2]
        ans = 0
        print(temp)
        remainder = temp[0] % x
        for i in range(1,n):
            if temp[i]%x != remainder:
                return -1
        for i in temp:
            ans += abs(i-median)//x
        return ans
