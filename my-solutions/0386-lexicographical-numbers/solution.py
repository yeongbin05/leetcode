class Solution(object):
    def lexicalOrder(self, n):
        # 내풀이
        # arr = sorted([str(i) for i in range(1,n+1)])
        # return map(int,arr)
        
        result = []
        def dfs(current):
            if current > n:
                return
            result.append(current)
            for i in range(10):
                next_num = current * 10 + i
                if next_num > n:
                    break
                dfs(next_num)
        
        for i in range(1, 10):
            dfs(i)
        
        return result
