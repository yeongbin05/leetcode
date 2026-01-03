class Solution:
    def numOfWays(self, n: int) -> int:
        cnt_5,cnt_4 = 6,6
        modulo = (10**9 + 7)
        for i in range(n-1):
            temp_cnt_5 = (cnt_5 * 3 + cnt_4 * 2 ) % modulo
            temp_cnt_4 = (cnt_5 * 2 + cnt_4 * 2) % modulo
            cnt_5 = temp_cnt_5 
            cnt_4 = temp_cnt_4 
        
        return (cnt_5 + cnt_4) % modulo
