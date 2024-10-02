class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        temp_arr = sorted(set(arr))
        dic = {}
        cnt = 1
        length = len(arr)
        ans = [0] * length
        for i in temp_arr:
            dic[i] = cnt
            cnt += 1
        
        for i in range(length):
            ans[i] = dic[arr[i]]

        return ans

