class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        dic = {}
        for i in arr :
            if i in dic:
                dic[i] += 1
            else :
                dic[i] = 1
        temp = 0
        for i,j in dic.items():

            if j == 1:
                temp+= 1

            if temp == k:
                return i

        return ""
