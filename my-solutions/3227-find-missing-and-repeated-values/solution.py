class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        nums = set(i for i in range(1,n**2+1))
        ans = []
        for i in range(n):
            for j in range(n):
                element = grid[i][j]
                if element in nums:
                    nums.remove(element)
                else:
                    ans.append(element)
        
        ans.append(nums.pop())

        return ans
