class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        temp = []
        def dfs(index):
            if len(temp) == k:
                ans.append(temp.copy())
                return

            for i in range(index,n+1):
                temp.append(i)
                dfs(i+1)
                temp.pop()

        dfs(1)
        print(ans)
        return ans
