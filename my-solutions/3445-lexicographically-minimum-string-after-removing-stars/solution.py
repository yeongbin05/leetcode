import heapq
class Solution:
    def clearStars(self, s: str) -> str:
        n = len(s)
        # 빼야할 알파벳이랑 위치 찾는 힙
        hq = []
        indices = {}
        ans = ""
        cnt = 0
        for i in range(n):
            if s[i] != "*":
                heapq.heappush(hq,(s[i],-i))
            else :
                alphabet,idx = heapq.heappop(hq)
                indices[-idx] = 1
                indices[i] = 1
                
        # print(indices)
        for i in range(n):
            if i not in indices:
                ans += s[i]
        return ans

