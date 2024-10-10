class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        dic = {}
        ans = []
        for i in nums :
            if i in dic:
                dic[i] += 1
            else :
                dic[i] = 1
        
        for i in nums:
            if dic[i] == 1:
                del dic[i]
            else :
                dic[i] -= 1
            cnt = 1
            print(dic)
            for j in dic:
                cnt *= j ** dic[j]
            ans.append(cnt)
            if i not in dic :
                dic[i] = 1
            else :
                dic[i] += 1
            

        return ans
