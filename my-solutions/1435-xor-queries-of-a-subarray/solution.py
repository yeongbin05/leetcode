class Solution(object):
    def xorQueries(self, arr, queries):
        n = len(arr)
        m = len(queries)
        prefix = [0] * (n + 1)
        
        for i in range(n):
            prefix[i+1] = prefix[i] ^ arr[i]
        
        
        result = [0] * m
        # for i, j in queries:
        #     result(prefix[j + 1] ^ prefix[i])
        for i in range(m):
            result[i] = prefix[queries[i][1]+1] ^ prefix[queries[i][0]]
        
        return result
