class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans = 0
        n = len(blocks)
        for i in range(k):
            if blocks[i] == 'W':
                ans += 1
        start = 0 
        end = k-1
        temp = ans
        for i in range(n-k):
            # 현재 윈도우 안의 W갯수 temp
            if blocks[start] == 'W':
                temp -= 1
            if blocks[end+1] == 'W':
                temp += 1
            if temp < ans:
                ans = temp
            start += 1
            end += 1

        return ans

