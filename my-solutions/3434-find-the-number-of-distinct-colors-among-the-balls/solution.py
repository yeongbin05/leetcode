class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        dic_idx = {}
        dic_color = {}
        ans = []
        cnt = 0
        for query in queries:
            idx,color = query[0],query[1]
            if idx not in dic_idx:
                dic_idx[idx] = color
                if color in dic_color and dic_color[color] > 0:
                    dic_color[color] += 1
                else:
                    dic_color[color] = 1
                    cnt += 1

            else:
                dic_color[dic_idx[idx]] -= 1
                if dic_color[dic_idx[idx]] < 1:
                    cnt -= 1
                dic_idx[idx] = color
                if color in dic_color and dic_color[color] > 0:
                    dic_color[color] += 1
                else:
                    dic_color[color] = 1
                    cnt += 1
            ans.append(cnt)
        return ans
