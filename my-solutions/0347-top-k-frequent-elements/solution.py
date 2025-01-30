class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        
        dic = sorted(dic,key = lambda x : -dic[x])
        for i in range(k):
            ans.append(dic[i])
        return ans
