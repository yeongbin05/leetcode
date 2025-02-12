import heapq
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:        
            temp = 0
            for j in str(i):
                temp += int(j)
            if temp not in dic:
                dic[temp] = []
                
            
            heapq.heappush(dic[temp],-i)
        ans = 0
        for i in dic:
            if len(dic[i]) > 1:
                temp = 0
                # 가장 큰 값 2개 더하기
                temp += (-heapq.heappop(dic[i]))
                temp += (-heapq.heappop(dic[i]))
                if temp > ans:
                    ans = temp

        if ans == 0 :
            return -1
        else:
            return ans



    

