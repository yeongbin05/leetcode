class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else :
                dic[i] = 1

        ans = []
        cnt = 0
        for i,j in sorted(dic.items(),key = lambda x:-x[1]):
            ans.append(i)
            cnt += 1
            # print(i,j,dic)
            if cnt == k :
                return ans
